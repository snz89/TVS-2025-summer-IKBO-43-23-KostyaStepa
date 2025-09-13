import argparse
import os

import pygame

from core import console, emulator, input_box
from source.color import Color as Color

pygame.init()

icon = pygame.image.load("source/img/UNIX_GUI_icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("UNIX GUI emulation")


def execute_startup_script(script_path, archive_path):
    if os.path.exists(script_path):
        with open(script_path) as script_file:
            commands = script_file.readlines()
            for command in commands:
                command = command.strip()
                if command:
                    console.text_list.append(f"Executing command: {command}")
                    emulator.Emulator(archive_path).read_command(command)
    else:
        console.text_list.append(
            f"ERROR: Startup script {script_path} not found."
        )


def shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel(
    archive_path, script_path
):
    if not os.path.exists(archive_path):
        console.text_list.append(f"ERROR: Archive {archive_path} not found.")
        return

    clock = pygame.time.Clock()
    console_output = console.ConsoleOutput(25, 18, 90, 600, 375)

    emulator_instance = emulator.Emulator(
        archive_path
    )  # Создаем один экземпляр эмулятора
    inputbox = input_box.InputBox(
        10, 50, 615, 30, 25, emulator_instance
    )  # Передаем экземпляр эмулятора в InputBox
    done = False

    execute_startup_script(script_path, archive_path)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            inputbox.handle_event(event)

        screen.fill(Color.back_ground)
        console_output.draw(screen)
        inputbox.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UNIX GUI Emulation")
    parser.add_argument(
        "--archive", required=True, help="Path to virtual filesystem archive"
    )
    parser.add_argument(
        "--script", required=True, help="Path to startup script"
    )

    args = parser.parse_args()

    shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel(
        args.archive, args.script
    )
