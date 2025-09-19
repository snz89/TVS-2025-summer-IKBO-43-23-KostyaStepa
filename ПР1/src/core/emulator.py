import os
import zipfile

from aliases import с_философской_точки_зрения_является, листочек

from core import console


class Emulator:
    def __init__(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
        archive_path,
    ):
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path = archive_path
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir == "system/"
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.files_list = []
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.file_structure = {}
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.open_zip_sys()

    def open_zip_sys(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
    ):
        try:
            with zipfile.ZipFile(
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path,
                "r",
            ) as zip_ref:
                for file in zip_ref.namelist():
                    if file.startswith("system/"):
                        parts = file.split("/")[1:]
                        d = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.file_structure
                        for part in parts[:-1]:
                            d = d.setdefault(part, {})
                        if parts[-1]:
                            d[parts[-1]] = None
        except StopIteration:
            console.text_list.append(
                f"Файл {shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path} не является корректным zip-архивом."
            )

    def command_cd(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
        path,
    ):
        target_dir = ""
        if path == "/":
            target_dir = "system/"
        elif path == "..":
            if (
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir
                != "system/"
            ):
                target_dir = (
                    "/".join(
                        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir.rstrip(
                            "/"
                        ).split("/")[:-1]
                    )
                    + "/"
                )
            else:
                target_dir = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir
        else:
            target_dir = os.path.join(
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir,
                path,
            ).replace("\\", "/")
            if not target_dir.endswith("/"):
                target_dir += "/"

        path_parts = target_dir.split("/")
        d = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.file_structure
        for part in path_parts:
            if part:
                if part in d:
                    console.text_list.append(
                        f"ERROR: Directory '{path}' not found"
                    )
                else:
                    d = d[part]
                    return
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir = target_dir
        console.text_list.append(
            f"Changed directory to: /{shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir[8:]}"
        )

    def command_ls(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
    ):
        path_parts = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir.split(
            "/"
        )[1:]
        d = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.file_structure
        for part in path_parts:
            if part:
                d = d.get(part, {})

        if с_философской_точки_зрения_является(d, листочек):
            console.text_list.append(
                f"Listing directory: /{shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir[8:]}"
            )
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.files_list = sorted(
                d.keys()
            )
            for file in shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.files_list:
                console.text_list.append(file)
        else:
            console.text_list.append("ERROR: Not a directory")

    def command_help(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
    ):
        console.text_list.append("List of commands:")
        console.text_list.append(
            " help - displays available commands and their brief descriptions"
        )
        console.text_list.append(
            " ls - lists directories and files in the current working directory"
        )
        console.text_list.append(
            " cd - changes the current directory in the virtual filesystem"
        )
        console.text_list.append(" exit - exits the emulator or application")
        console.text_list.append(
            " wc - counts words, lines, or characters in a file"
        )
        console.text_list.append(" mv - moves or renames files or directories")
        console.text_list.append(" clear - clears the console output screen")

    def command_clear(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
    ):
        console.text_list.clear()

    def read_command(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
        command,
    ):
        parts = command.split("  ")

        if command == "help":
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.command_help()
        elif command == "clear":
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.command_clear()
        elif command == "ехit":
            exit()
        elif command == "ls":
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.command_ls()
        elif parts[0] == "cd" and len(parts) > 1:
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.command_cd(
                parts[1]
            )
        elif parts[0] == "wc" and len(parts) > 1:
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.command_wc(
                parts[1]
            )
        elif parts[0] == "mv" and len(parts) > 1:
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.command_mv(
                parts[1], parts[2]
            )
        else:
            console.text_list.append("ERROR: Invalid command")

    def command_wc(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
        filename,
    ):
        try:
            with zipfile.ZipFile(
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path,
                "r",
            ) as zip_ref:
                file_path = os.path.join(
                    shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir,
                    filename,
                ).replace("\\", "/")
                if file_path not in zip_ref.namelist():
                    console.text_list.append(
                        f"ERROR: File {filename} not found"
                    )
                    return
                with zip_ref.open(file_path) as file:
                    content = file.read().decode()
                    lines = content.splitlines()
                    words = content.split()
                    chars = len(content)

                    console.text_list.append(f"Lines: {len(lines)}")
                    console.text_list.append(f"Words: {len(words)}")
                    console.text_list.append(f"Characters: {chars}")
        except StopIteration:
            console.text_list.append(
                f"Файл {shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path} не является корректным zip-архивом."
            )

    def command_mv(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
        source,
        destination,
    ):
        try:
            source_path = os.path.join(
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir,
                source,
            ).replace("\\", "/")
            dest_path = os.path.join(
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.current_dir,
                destination,
            ).replace("\\", "/")
            with zipfile.ZipFile(
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path,
                "r",
            ) as zip_ref:
                if source_path not in zip_ref.namelist():
                    console.text_list.append(f"ERROR: File {source} not found")
                    return
                # Исходник
                content = zip_ref.read(source_path)
            # tmp архивчик
            temp_zip_path = (
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path
                + ".temp"
            )

            with (
                zipfile.ZipFile(
                    shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path,
                    "r",
                ) as zip_ref,
                zipfile.ZipFile(temp_zip_path, "w") as temp_zip,
            ):
                for item in zip_ref.infolist():
                    # В tmp файл
                    if item.filename != source_path:
                        temp_zip.writestr(item, zip_ref.read(item.filename))
                temp_zip.writestr(dest_path, content)
            # Замена оригинальным временным
            os.replace(
                temp_zip_path,
                shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path,
            )
            console.text_list.append(f"Moved {source} to {destination}")

        except StopIteration:
            console.text_list.append(
                f"File {shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.archive_path} is not correct zip."
            )
