import pygame

from core import console
from source.color import Color

console_output = console.ConsoleOutput


class InputBox:
    def __init__(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
        x,
        y,
        w,
        h,
        font_size,
        emulator_instance,
    ):
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.rect = pygame.Rect(
            x, y, w, h
        )
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.color_inactive = (
            0,
            0,
            0,
        )
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.color_active = Color.anactice_white
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.color = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.color_inactive
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.active = False
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.text = ""
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.font = pygame.font.Font(
            None, font_size
        )
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.txt_surface = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.font.render(
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.text,
            True,
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.color,
        )
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.min_w = w
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.emulator = emulator_instance

    def handle_event(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
        event,
    ):
        global history_step
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.rect.collidepoint(
                event.pos
            ):
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.active = not shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.active
            else:
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.active = False
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.color = (
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.color_active
                if shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.active
                else shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.color_inactive
            )

        if event.type == pygame.KEYDOWN:
            if shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.active:
                if event.key == pygame.K_RETURN:
                    if (
                        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.text
                        != ""
                    ):
                        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.emulator.read_command(
                            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.text
                        )  # Используем существующий объект эмулятора
                        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.text = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.text[
                        :-1
                    ]
                elif event.key == pygame.K_ESCAPE:
                    pass
                else:
                    shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.text += event.unicode
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.txt_surface = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.font.render(
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.text,
            True,
            Color.text_white,
        )

    def draw(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
        screen,
    ):
        screen.blit(
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.txt_surface,
            (
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.rect.y
                + 5,
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.rect.x
                + 5,
            ),
        )
        pygame.draw.rect(
            screen,
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.color,
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.rect,
            2,
        )
