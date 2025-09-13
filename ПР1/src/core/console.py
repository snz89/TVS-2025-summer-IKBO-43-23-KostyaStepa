import pygame
from source.color import Color

text_list: list[str] = []
text_animation_step = 1
text_animation_y = 20


class ConsoleOutput:
    def __init__(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel
        font_size,
        x,
        y,
        w,
        h,
    ):
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.rect = pygame.Rect(
            x, y, w, h
        )
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.font = pygame.font.Font(
            None, font_size
        )
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.line_height = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.font.get_height()

    def draw(
        shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel,
        screen,
    ):
        pygame.draw.rect(
            screen,
            Color.black,
            shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.rect,
            2,
        )

        if len(text_list) > 18:
            text_list.pop(0)

        for i in range(len(text_list)):
            img = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.font.render(
                text_list[i], True, Color.text_white
            )
            screen.blit(img, (300, 100 + 20 * i))

        img = shel_medved_po_lesu_vidit_kamen_a_nem_nadpis_nalevo_pojdyosh_v_mashine_sgorish_napravo_pojdyosh_v_mashine_sgorish_prjamo_pojdyosh_v_mashine_sgorish_poshel_medved_nazad_vidit_mashina_gorit_sel_v_nee_i_sgorel.font.render(
            "Type command", True, Color.text_white
        )
        screen.blit(img, (225, text_animation_y))
