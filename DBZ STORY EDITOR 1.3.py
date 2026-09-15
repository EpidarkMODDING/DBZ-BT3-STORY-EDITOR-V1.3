import csv
import io
import math
import os
import re
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, ttk

# --- DICCIONARIOS DE BT3 DE LA HERRAMIENTA 1 ---

BGMS = {
    "0": "000 - The Meteor",
    "1": "001 - Vital Burner",
    "2": "002 - Innocent World",
    "3": "003 - After The Fire",
    "4": "004 - Sweet Vibration",
    "5": "005 - Survive",
    "6": "006 - Heat Capacity",
    "7": "007 - Overture",
    "8": "008 - Shine",
    "9": "009 - Power Scale",
    "10": "010 - Edge of Spirit",
    "11": "011 - Caution!",
    "12": "012 - Menace",
    "13": "013 - Hot Soul",
    "14": "014 - High And Scream",
    "15": "015 - Shootout in Meteor",
    "16": "016 - Dynamite Battle",
    "17": "017 - Burnin' Up",
    "18": "018 - Wild Rush",
    "19": "019 - Evolution",
    "20": "020 - Super Survivor Full ver.",
    "21": "021 - Super Survivor Short ver.",
    "22": "022 - Super Survivor Instrumental Full ver.",
    "23": "023 - Super Survivor Instrumental Short ver.",
}

MAPS = {
    "0": "00 - Tierra baldía - Mediodía",
    "1": "01 - Zona rocosa - Mediodía",
    "2": "02 - Planeta Namek",
    "3": "03 - Namek moribundo",
    "4": "04 - Escenario del Torneo Mundial - Mediodía",
    "5": "05 - Torre de Karin",
    "6": "06 - Arena de los Juegos de Cell - Atardecer",
    "7": "07 - Mundo del Supremo Kai",
    "8": "08 - Sala del Tiempo",
    "9": "09 - Ruinas de la ciudad - Mediodía",
    "10": "10 - Camino montañoso - Mediodía",
    "11": "11 - Islas",
    "12": "12 - Casa Kame",
    "13": "13 - Planeta - Noche",
    "14": "14 - Glaciar",
    "15": "15 - Tierra devastada",
    "16": "16 - Espacio exterior",
    "17": "17 - Villa Pingüino",
    "18": "18 - Infierno",
    "19": "19 - Desierto - Mediodía",
    "20": "20 - Castillo del Rey",
    "21": "21 - Torre Músculo",
    "22": "22 - Monte Paozu",
    "23": "23 - Tierra baldía - Atardecer",
    "24": "24 - Tierra baldía - Noche",
    "25": "25 - Zona rocosa - Atardecer",
    "26": "26 - Zona rocosa - Noche",
    "27": "27 - Escenario del Torneo Mundial - Atardecer",
    "28": "28 - Arena de los Juegos de Cell - Mediodía",
    "29": "29 - Ruinas de la ciudad - Atardecer",
    "30": "30 - Ruinas de la ciudad - Noche",
    "31": "31 - Desierto - Atardecer",
    "32": "32 - Desierto - Noche",
    "33": "33 - Camino montañoso - Atardecer",
    "34": "34 - Planeta - Atardecer",
}

CHARACTERS_STORY = {
"0": "000 - Goku (Inicial)",
    "1": "001 - Goku (Medio)",
    "2": "002 - Goku (Medio) - Super Saiyajin",
    "3": "003 - Goku (Final)",
    "4": "004 - Goku (Final) - Super Saiyajin",
    "5": "005 - Goku (Final) - Super Saiyajin 2",
    "6": "006 - Goku (Final) - Super Saiyajin 3",
    "7": "007 - Goku (GT)",
    "8": "008 - Goku (GT) - Super Saiyajin",
    "9": "009 - Goku (GT) - Super Saiyajin 3",
    "10": "010 - Goku (GT) - Super Saiyajin 4",
    "11": "011 - Pequeño Goku",
    "12": "012 - Gran Mono",
    "13": "013 - Pequeño Gohan",
    "14": "014 - Adolescente Gohan",
    "15": "015 - Adolescente Gohan - Super Saiyajin",
    "16": "016 - Adolescente Gohan - Super Saiyajin 2",
    "17": "017 - Adulto Gohan",
    "18": "018 - Adulto Gohan - Super Saiyajin",
    "19": "019 - Adulto Gohan - Super Saiyajin 2",
    "20": "020 - Gran Saiyaman",
    "21": "021 - Gohan Definitivo",
    "22": "022 - Piccolo (Inicial)",
    "23": "023 - Piccolo (Final)",
    "24": "024 - Nail",
    "25": "025 - Krilin",
    "26": "026 - Yamcha",
    "27": "027 - Tenshinhan",
    "28": "028 - Chaoz",
    "29": "029 - Vegeta (Scouter)",
    "30": "030 - Gran Mono Vegeta",
    "31": "031 - Vegeta",
    "32": "032 - Vegeta - Super Saiyajin",
    "33": "033 - Super Vegeta",
    "34": "034 - Vegeta (segunda forma)",
    "35": "035 - Vegeta (segunda forma) - Super Saiyajin",
    "36": "036 - Vegeta (segunda forma) - Super Saiyajin 2",
    "37": "037 - Vegeta (Final) - Majin",
    "38": "038 - Vegeta (segunda forma) - Super Saiyajin 4",
    "39": "039 - Trunks (Espada)",
    "40": "040 - Trunks (Espada) - Super Saiyajin",
    "41": "041 - Trunks",
    "42": "042 - Trunks - Super Saiyajin",
    "43": "043 - Super Trunks",
    "44": "044 - Pequeño Trunks",
    "45": "045 - Pequeño Trunks - Super Saiyajin",
    "46": "046 - Goten",
    "47": "047 - Goten - Super Saiyajin",
    "48": "048 - Gotenks",
    "49": "049 - Gotenks - Super Saiyajin",
    "50": "050 - Gotenks - Super Saiyajin 3",
    "51": "051 - Vegetto",
    "52": "052 - Super Vegetto",
    "53": "053 - Super Gogeta",
    "54": "054 - Gogeta - Super Saiyajin 4",
    "55": "055 - Mr. Satán",
    "56": "056 - Videl",
    "57": "057 - Gran Saiyaman 2",
    "58": "058 - Kaio-shin",
    "59": "059 - Kibitoshin",
    "60": "060 - Yajirobe",
    "61": "061 - Paikuhan",
    "62": "062 - Tapion",
    "63": "063 - Pan",
    "64": "064 - Uub",
    "65": "065 - Majuub",
    "66": "066 - Maestro Roshi",
    "67": "067 - Maestro Roshi - Máximo Poder",
    "68": "068 - Abuelo Gohan",
    "69": "069 - Nam",
    "70": "070 - Androide #8",
    "71": "071 - Rey Vegeta",
    "72": "072 - Gran Mono Rey Vegeta",
    "73": "073 - Bardock",
    "74": "074 - Gran Mono Bardock",
    "75": "075 - Fasha",
    "76": "076 - Gran Mono Fasha",
    "77": "077 - Raditz",
    "78": "078 - Gran Mono Raditz",
    "79": "079 - Saibaman",
    "80": "080 - Nappa",
    "81": "081 - Gran Mono Nappa",
    "82": "082 - Zarbon",
    "83": "083 - Zarbon - Post-transformación",
    "84": "084 - Dodoria",
    "85": "085 - Cui",
    "86": "086 - Capitán Ginyu",
    "87": "087 - Recoome",
    "88": "088 - Burter",
    "89": "089 - Jeice",
    "90": "090 - Guldo",
    "91": "091 - Freezer - 1.ª forma",
    "92": "092 - Freezer - 2.ª forma",
    "93": "093 - Freezer - 3.ª forma",
    "94": "094 - Freezer - Forma final",
    "95": "095 - Freezer - Máximo poder",
    "96": "096 - Mecha Freezer",
    "97": "097 - King Cold",
    "98": "098 - Appule",
    "99": "099 - Soldado de Freezer",
    "100": "100 - Androide #16",
    "101": "101 - Androide #17",
    "102": "102 - Androide #18",
    "103": "103 - Androide #19",
    "104": "104 - Dr. Gero",
    "105": "105 - Cell - 1.ª forma",
    "106": "106 - Cell - 2.ª forma",
    "107": "107 - Cell - Forma perfecta",
    "108": "108 - Cell - Perfecto",
    "109": "109 - Cell Jr.",
    "110": "110 - Babidi",
    "111": "111 - Rey Demonio Dabura",
    "112": "112 - Majin Buu",
    "113": "113 - Majin Buu (Maldad pura)",
    "114": "114 - Super Buu",
    "115": "115 - Super Buu - Absorbido a Gotenks",
    "116": "116 - Super Buu - Absorbido a Gohan",
    "117": "117 - Pequeño Buu",
    "118": "118 - Garlic Jr.",
    "119": "119 - Super Garlic Jr.",
    "120": "120 - Dr. Wheelo",
    "121": "121 - Turles",
    "122": "122 - Gran Mono Turles",
    "123": "123 - Slug",
    "124": "124 - Slug - Gigante",
    "125": "125 - Salza",
    "126": "126 - Cooler",
    "127": "127 - Cooler - Forma final",
    "128": "128 - Meta-Cooler",
    "129": "129 - Androide #13",
    "130": "130 - Androide #13 - Fusión",
    "131": "131 - Broly",
    "132": "132 - Broly - Super Saiyajin",
    "133": "133 - Broly - Super Saiyajin Legendario",
    "134": "134 - Zangya",
    "135": "135 - Bojack",
    "136": "136 - Bojack - Máximo poder",
    "137": "137 - Janemba",
    "138": "138 - Super Janemba",
    "139": "139 - Hirudegarn",
    "140": "140 - Baby Vegeta",
    "141": "141 - Super Baby 1",
    "142": "142 - Super Baby 2",
    "143": "143 - Gran Mono Baby",
    "144": "144 - Super 17",
    "145": "145 - Nuova Shenron",
    "146": "146 - Syn Shenron",
    "147": "147 - Omega Shenron",
    "148": "148 - Tao Pai Pai",
    "149": "149 - Cíborg Tao",
    "150": "150 - General Blue",
    "151": "151 - Devilman",
    "152": "152 - Máquina de Pilaf",
    "153": "153 - Máquina de Pilaf - Fusión",
    "154": "154 - Tambourine",
    "155": "155 - Rey Demonio Piccolo",
    "156": "156 - Arale",
    "157": "157 - Chi-Chi",
    "158": "158 - Spopovich",
    "159": "159 - Gohan del Futuro",
    "160": "160 - Gohan del Futuro - Super Saiyajin"
}

COSTUMES = {
    "0": "Traje 1",
    "1": "Traje 2",
    "2": "Traje 3",
    "3": "Traje 4",
    "4": "Traje 5",
    "5": "Traje 6",
    "6": "Traje 7",
    "7": "Traje 8",
}

EMPTY_SLOT = "[Inactivo / Sin Personaje]"

ANIMATIONS = {
    "000": "000_suelo.canm",
    "001": "001_suelo_cansado.canm",
    "002": "002_mover_lejos_entrada.canm",
    "003": "003_mover_lejos_bucle.canm",
    "004": "004_mover_lejos_izquierda_entrada.canm",
    "005": "005_mover_lejos_izquierda_bucle.canm",
    "006": "006_mover_lejos_derecha_entrada.canm",
    "007": "007_mover_lejos_derecha_bucle.canm",
    "008": "008_mover_cerca_frente.canm",
    "009": "009_mover_cerca_atras.canm",
    "00A": "00A_mover_cerca_izquierda.canm",
    "00B": "00B_mover_cerca_derecha.canm",
    "00C": "00C_carrera_frente_entrada.canm",
    "00D": "00D_carrera_frente_bucle.canm",
    "00E": "00E_carrera_frente_salida.canm",
    "00F": "00F_carrera_izquierda_entrada.canm",
    "010": "010_carrera_izquierda_bucle.canm",
    "011": "011_carrera_izquierda_salida.canm",
    "012": "012_carrera_derecha_entrada.canm",
    "013": "013_carrera_derecha_bucle.canm",
    "014": "014_carrera_derecha_salida.canm",
    "015": "015_embestida_romper_entrada.canm",
    "016": "016_embestida_romper_bucle.canm",
    "017": "017_embestida_romper_salida.canm",
    "018": "018_doble_embestida_entrada.canm",
    "019": "019_doble_embestida_bucle.canm",
    "01A": "01A_doble_embestida_salida.canm",
    "01B": "01B_esquivar_frente.canm",
    "01C": "01C_esquivar_atras.canm",
    "01D": "01D_esquivar_izquierda.canm",
    "01E": "01E_esquivar_derecha.canm",
    "01F": "01F_esquivar_salida.canm",
    "020": "020_salto_entrada.canm",
    "021": "021_salto_subida.canm",
    "022": "022_salto_bajada.canm",
    "023": "023_salto_salida.canm",
    "024": "024_ascenso_entrada.canm",
    "025": "025_ascenso_salida.canm",
    "026": "026_volar.canm",
    "027": "027_volar_cansado.canm",
    "028": "028_volar_esquivar_atras.canm",
    "029": "029_volar_esquivar_izquierda.canm",
    "02A": "02A_volar_esquivar_derecha.canm",
    "02B": "02B_volar_arriba.canm",
    "02C": "02C_volar_abajo_entrada.canm",
    "02D": "02D_volar_abajo_bucle.canm",
    "02E": "02E_volar_subida_rapida_entrada.canm",
    "02F": "02F_volar_subida_rapida_bucle.canm",
    "030": "030_volar_subida_rapida_salida.canm",
    "031": "031_volar_bajada_rapida_entrada.canm",
    "032": "032_volar_bajada_rapida_bucle.canm",
    "033": "033_volar_bajada_rapida_salida.canm",
    "034": "034_carga_entrada.canm",
    "035": "035_carga_bucle.canm",
    "036": "036_carga_maxima.canm",
    "037": "037_golpe_01.canm",
    "038": "038_golpe_02.canm",
    "039": "039_golpe_03.canm",
    "03A": "03A_golpe_04.canm",
    "03B": "03B_golpe_05.canm",
    "03C": "03C_golpe_06.canm",
    "03D": "03D_golpe_07.canm",
    "03E": "03E_golpe_08.canm",
    "03F": "03F_golpe_09.canm",
    "040": "040_golpe_10.canm",
    "041": "041_golpe_elevado_entrada.canm",
    "042": "042_golpe_elevado_bucle.canm",
    "043": "043_golpe_elevado_salida.canm",
    "044": "044_corte_tierra_entrada.canm",
    "045": "045_corte_tierra_bucle.canm",
    "046": "046_corte_tierra_salida.canm",
    "047": "047_golpe_pesado_entrada.canm",
    "048": "048_golpe_pesado_bucle.canm",
    "049": "049_golpe_pesado_salida.canm",
    "04A": "04A_golpe_cargado_frente_entrada.canm",
    "04B": "04B_golpe_cargado_frente_bucle.canm",
    "04C": "04C_golpe_cargado_frente_salida.canm",
    "04D": "04D_combo_golpe_entrada.canm",
    "04E": "04E_combo_golpe_bucle.canm",
    "04F": "04F_combo_golpe_salida.canm",
    "050": "050_golpe_cargado_arriba_entrada.canm",
    "051": "051_golpe_cargado_arriba_bucle.canm",
    "052": "052_golpe_cargado_arriba_salida.canm",
    "053": "053_golpe_cargado_abajo_entrada.canm",
    "054": "054_golpe_cargado_abajo_bucle.canm",
    "055": "055_golpe_cargado_abajo_salida.canm",
    "056": "056_golpe_cargado_izquierda_entrada.canm",
    "057": "057_golpe_cargado_izquierda_bucle.canm",
    "058": "058_golpe_cargado_izquierda_salida.canm",
    "059": "059_golpe_cargado_derecha_entrada.canm",
    "05A": "05A_golpe_cargado_derecha_bucle.canm",
    "05B": "05B_golpe_cargado_derecha_salida.canm",
    "05C": "05C_golpe_rapido_frente_entrada.canm",
    "05D": "05D_golpe_rapido_frente_bucle.canm",
    "05E": "05E_golpe_rapido_frente_salida.canm",
    "05F": "05F_golpe_rapido_arriba_entrada.canm",
    "060": "060_golpe_rapido_arriba_bucle.canm",
    "061": "061_golpe_rapido_arriba_salida.canm",
    "062": "062_golpe_rapido_abajo_entrada.canm",
    "063": "063_golpe_rapido_abajo_bucle.canm",
    "064": "064_golpe_rapido_abajo_salida.canm",
    "065": "065_golpe_rapido_izquierda_entrada.canm",
    "066": "066_golpe_rapido_izquierda_bucle.canm",
    "067": "067_golpe_rapido_izquierda_salida.canm",
    "068": "068_golpe_rapido_derecha_entrada.canm",
    "069": "069_golpe_rapido_derecha_bucle.canm",
    "06A": "06A_golpe_rapido_derecha_salida.canm",
    "06B": "06B_golpe_embestida_entrada.canm",
    "06C": "06C_golpe_embestida_bucle.canm",
    "06D": "06D_golpe_embestida_salida.canm",
    "06E": "06E_golpe_salto_entrada.canm",
    "06F": "06F_golpe_salto_bucle.canm",
    "070": "070_golpe_salto_salida.canm",
    "071": "071_ki_frente_entrada.canm",
    "072": "072_ki_frente_bucle.canm",
    "073": "073_ki_disparo_arriba_entrada.canm",
    "074": "074_ki_disparo_arriba_bucle.canm",
    "075": "075_ki_disparo_abajo_entrada.canm",
    "076": "076_ki_disparo_abajo_bucle.canm",
    "077": "077_ki_embestida_frente.canm",
    "078": "078_ki_embestida_izquierda.canm",
    "079": "079_ki_embestida_derecha.canm",
    "07A": "07A_ki_salto_disparo.canm",
    "07B": "07B_ki_cargado_frente_entrada.canm",
    "07C": "07C_ki_cargado_frente_bucle.canm",
    "07D": "07D_ki_cargado_frente_salida.canm",
    "07E": "07E_ki_cargado_arriba_entrada.canm",
    "07F": "07F_ki_cargado_arriba_bucle.canm",
    "080": "080_ki_cargado_arriba_salida.canm",
    "081": "081_ki_cargado_abajo_entrada.canm",
    "082": "082_ki_cargado_abajo_bucle.canm",
    "083": "083_ki_cargado_abajo_salida.canm",
    "084": "084_ki_embestida_cargada_frente_entrada.canm",
    "085": "085_ki_embestida_cargada_frente_bucle.canm",
    "086": "086_ki_embestida_cargada_frente_salida.canm",
    "087": "087_ki_embestida_cargada_izquierda_entrada.canm",
    "088": "088_ki_embestida_cargada_izquierda_bucle.canm",
    "089": "089_ki_embestida_cargada_izquierda_salida.canm",
    "08A": "08A_ki_embestida_cargada_derecha_entrada.canm",
    "08B": "08B_ki_embestida_cargada_derecha_bucle.canm",
    "08C": "08C_ki_embestida_cargada_derecha_salida.canm",
    "08D": "08D_ki_salto_cargado_entrada.canm",
    "08E": "08E_ki_salto_cargado_bucle.canm",
    "08F": "08F_ki_salto_cargado_salida.canm",
    "090": "090_cañon_kiai_entrada.canm",
    "091": "091_cañon_kiai_bucle.canm",
    "092": "092_cañon_kiai_salida.canm",
    "093": "093_patada_voladora.canm",
    "094": "094_agarre_entrada.canm",
    "095": "095_agarre_bucle.canm",
    "096": "096_lanzamiento_evento.canm",
    "097": "097_lanzamiento_enemigo.canm",
    "098": "098_agarre_salida.canm",
    "099": "099_lanzamiento_abajo_entrada.canm",
    "09A": "09A_lanzamiento_abajo_bucle.canm",
    "09B": "09B_lanzamiento_abajo_salida.canm",
    "09C": "09C_bloqueo_lanzamiento_entrada.canm",
    "09D": "09D_bloqueo_lanzamiento_salida.canm",
    "09E": "09E_dano_frente.canm",
    "09F": "09F_dano_izquierda.canm",
    "0A0": "0A0_dano_derecha.canm",
    "0A1": "0A1_dano_atras.canm",
    "0A2": "0A2_dano_volando_frente.canm",
    "0A3": "0A3_dano_volando_izquierda.canm",
    "0A4": "0A4_dano_volando_derecha.canm",
    "0A5": "0A5_dano_volando_atras.canm",
    "0A6": "0A6_dano_11.canm",
    "0A7": "0A7_dano_12.canm",
    "0A8": "0A8_dano_13.canm",
    "0A9": "0A9_dano_14.canm",
    "0AA": "0AA_dano_15.canm",
    "0AB": "0AB_dano_16.canm",
    "0AC": "0AC_dano_17.canm",
    "0AD": "0AD_dano_18.canm",
    "0AE": "0AE_dano_pesado_frente.canm",
    "0AF": "0AF_dano_pesado_atras.canm",
    "0B0": "0B0_dano_21.canm",
    "0B1": "0B1_dano_22.canm",
    "0B2": "0B2_dano_23.canm",
    "0B3": "0B3_dano_24.canm",
    "0B4": "0B4_dano_25.canm",
    "0B5": "0B5_dano_26.canm",
    "0B6": "0B6_dano_27.canm",
    "0B7": "0B7_paralisis.canm",
    "0B8": "0B8_quebrantaguardia.canm",
    "0B9": "0B9_dano_tumbado_arriba.canm",
    "0BA": "0BA_dano_tumbado_abajo.canm",
    "0BB": "0BB_dano_explosion_frontal.canm",
    "0BC": "0BC_dano_explosion_trasera.canm",
    "0BD": "0BD_dano_rodar_atras_entrada.canm",
    "0BE": "0BE_dano_rodar_atras_bucle.canm",
    "0BF": "0BF_dano_rodar_atras_salida.canm",
    "0C0": "0C0_dano_rodar_entrada.canm",
    "0C1": "0C1_dano_rodar_bucle.canm",
    "0C2": "0C2_dano_rodar_salida.canm",
    "0C3": "0C3_dano_golpe_cargado_entrada.canm",
    "0C4": "0C4_dano_golpe_cargado_bucle.canm",
    "0C5": "0C5_dano_golpe_cargado_salida.canm",
    "0C6": "0C6_dano_caida_1.canm",
    "0C7": "0C7_dano_caida_2.canm",
    "0C8": "0C8_dano_caida_3.canm",
    "0C9": "0C9_dano_caida_4.canm",
    "0CA": "0CA_dano_28.canm",
    "0CB": "0CB_dano_29.canm",
    "0CC": "0CC_dano_30.canm",
    "0CD": "0CD_dano_31.canm",
    "0CE": "0CE_dano_32.canm",
    "0CF": "0CF_dano_33.canm",
    "0D0": "0D0_dano_34.canm",
    "0D1": "0D1_dano_35.canm",
    "0D2": "0D2_dano_tumbado_paralizado_entrada.canm",
    "0D3": "0D3_dano_tumbado_paralizado_bucle.canm",
    "0D4": "0D4_dano_tumbado_cansado_entrada.canm",
    "0D5": "0D5_dano_tumbado_cansado_bucle.canm",
    "0D6": "0D6_dano_tumbado_cansado_salida.canm",
    "0D7": "0D7_dano_flotar_agua_entrada.canm",
    "0D8": "0D8_dano_flotar_agua_bucle.canm",
    "0D9": "0D9_dano_caida_muerte.canm",
    "0DA": "0DA_dano_36.canm",
    "0DB": "0DB_dano_37.canm",
    "0DC": "0DC_dano_corte_tierra_entrada.canm",
    "0DD": "0DD_dano_corte_tierra_bucle.canm",
    "0DE": "0DE_dano_esquivar_sonico_1.canm",
    "0DF": "0DF_dano_esquivar_sonico_2.canm",
    "0E0": "0E0_dano_martillo_rodante_entrada.canm",
    "0E1": "0E1_dano_martillo_rodante_bucle.canm",
    "0E2": "0E2_levantarse_entrada.canm",
    "0E3": "0E3_levantarse_bucle.canm",
    "0E4": "0E4_levantarse_salida.canm",
    "0E5": "0E5_levantarse_4.canm",
    "0E6": "0E6_levantarse_5.canm",
    "0E7": "0E7_levantarse_6.canm",
    "0E8": "0E8_dano_38.canm",
    "0E9": "0E9_dano_39.canm",
    "0EA": "0EA_dano_40.canm",
    "0EB": "0EB_dano_41.canm",
    "0EC": "0EC_dano_contraz_1.canm",
    "0ED": "0ED_dano_contraz_2.canm",
    "0EE": "0EE_dano_42.canm",
    "0EF": "0EF_dano_43.canm",
    "0F0": "0F0_bloqueo_entrada.canm",
    "0F1": "0F1_bloqueo_bucle.canm",
    "0F2": "0F2_bloqueo_arriba_entrada.canm",
    "0F3": "0F3_bloqueo_arriba_bucle.canm",
    "0F4": "0F4_bloqueo_abajo_entrada.canm",
    "0F5": "0F5_bloqueo_abajo_bucle.canm",
    "0F6": "0F6_bloqueo_golpe_entrada.canm",
    "0F7": "0F7_bloqueo_golpe_bucle.canm",
    "0F8": "0F8_parry_combo_postura.canm",
    "0F9": "0F9_parry_combo_golpe.canm",
    "0FA": "0FA_parry_disparo_ki_1.canm",
    "0FB": "0FB_parry_disparo_ki_2.canm",
    "0FC": "0FC_parry_disparo_ki_3.canm",
    "0FD": "0FD_parry_disparo_ki_4.canm",
    "0FE": "0FE_parry_disparo_ki_5.canm",
    "0FF": "0FF_recuperacion_rapida_entrada.canm",
    "100": "100_recuperacion_rapida_bucle.canm",
    "101": "101_recuperacion_rapida_enemigo_entrada.canm",
    "102": "102_recuperacion_rapida_enemigo_bucle.canm",
    "103": "103_habilidad_001.canm",
    "104": "104_habilidad_002.canm",
    "105": "105_habilidad_003_entrada.canm",
    "106": "106_habilidad_003_carga.canm",
    "107": "107_habilidad_003_disparo1.canm",
    "108": "108_habilidad_003_disparo2.canm",
    "109": "109_habilidad_003_bucle1.canm",
    "10A": "10A_habilidad_003_bucle2.canm",
    "10B": "10B_habilidad_003_salida.canm",
    "10C": "10C_habilidad_003_entrada_arriba.canm",
    "10D": "10D_habilidad_003_carga_arriba.canm",
    "10E": "10E_habilidad_003_disparo1_arriba.canm",
    "10F": "10F_habilidad_003_disparo2_arriba.canm",
    "110": "110_habilidad_003_bucle3_arriba.canm",
    "111": "111_habilidad_003_bucle4_arriba.canm",
    "112": "112_habilidad_003_salida_arriba.canm",
    "113": "113_habilidad_003_entrada_abajo.canm",
    "114": "114_habilidad_003_carga_abajo.canm",
    "115": "115_habilidad_003_disparo1_abajo.canm",
    "116": "116_habilidad_003_disparo2_abajo.canm",
    "117": "117_habilidad_003_bucle3_abajo.canm",
    "118": "118_habilidad_003_bucle4_abajo.canm",
    "119": "119_habilidad_003_salida_abajo.canm",
    "11A": "11A_habilidad_003_22.canm",
    "11B": "11B_habilidad_003_23.canm",
    "11C": "11C_habilidad_003_evento_1.canm",
    "11D": "11D_habilidad_003_evento_2.canm",
    "11E": "11E_habilidad_003_evento_3.canm",
    "11F": "11F_habilidad_003_evento_4.canm",
    "120": "120_habilidad_003_evento_5.canm",
    "121": "121_habilidad_003_enemigo_1.canm",
    "122": "122_habilidad_003_enemigo_2.canm",
    "123": "123_habilidad_003_enemigo_3.canm",
    "124": "124_habilidad_003_enemigo_4.canm",
    "125": "125_habilidad_003_enemigo_5.canm",
    "126": "126_habilidad_003_34.canm",
    "127": "127_habilidad_004_entrada.canm",
    "128": "128_habilidad_004_carga.canm",
    "129": "129_habilidad_004_disparo1.canm",
    "12A": "12A_habilidad_004_disparo2.canm",
    "12B": "12B_habilidad_004_bucle1.canm",
    "12C": "12C_habilidad_004_bucle2.canm",
    "12D": "12D_habilidad_004_salida.canm",
    "12E": "12E_habilidad_004_entrada_arriba.canm",
    "12F": "12F_habilidad_004_carga_arriba.canm",
    "130": "130_habilidad_004_disparo1_arriba.canm",
    "131": "131_habilidad_004_disparo2_arriba.canm",
    "132": "132_habilidad_004_bucle3_arriba.canm",
    "133": "133_habilidad_004_bucle4_arriba.canm",
    "134": "134_habilidad_004_salida_arriba.canm",
    "135": "135_habilidad_004_entrada_abajo.canm",
    "136": "136_habilidad_004_carga_abajo.canm",
    "137": "137_habilidad_004_disparo1_abajo.canm",
    "138": "138_habilidad_004_disparo2_abajo.canm",
    "139": "139_habilidad_004_bucle3_abajo.canm",
    "13A": "13A_habilidad_004_bucle4_abajo.canm",
    "13B": "13B_habilidad_004_salida_abajo.canm",
    "13C": "13C_habilidad_004_22.canm",
    "13D": "13D_habilidad_004_23.canm",
    "13E": "13E_habilidad_004_evento_1.canm",
    "13F": "13F_habilidad_004_evento_2.canm",
    "140": "140_habilidad_004_evento_3.canm",
    "141": "141_habilidad_004_evento_4.canm",
    "142": "142_habilidad_004_evento_5.canm",
    "143": "143_habilidad_004_enemigo_1.canm",
    "144": "144_habilidad_004_enemigo_2.canm",
    "145": "145_habilidad_004_enemigo_3.canm",
    "146": "146_habilidad_004_enemigo_4.canm",
    "147": "147_habilidad_004_enemigo_5.canm",
    "148": "148_habilidad_004_34.canm",
    "149": "149_habilidad_005_entrada.canm",
    "14A": "14A_habilidad_005_carga.canm",
    "14B": "14B_habilidad_005_disparo1.canm",
    "14C": "14C_habilidad_005_disparo2.canm",
    "14D": "14D_habilidad_005_bucle1.canm",
    "14E": "14E_habilidad_005_bucle2.canm",
    "14F": "14F_habilidad_005_salida.canm",
    "150": "150_habilidad_005_entrada_arriba.canm",
    "151": "151_habilidad_005_carga_arriba.canm",
    "152": "152_habilidad_005_disparo1_arriba.canm",
    "153": "153_habilidad_005_disparo2_arriba.canm",
    "154": "154_habilidad_005_bucle3_arriba.canm",
    "155": "155_habilidad_005_bucle4_arriba.canm",
    "156": "156_habilidad_005_salida_arriba.canm",
    "157": "157_habilidad_005_entrada_abajo.canm",
    "158": "158_habilidad_005_carga_abajo.canm",
    "159": "159_habilidad_005_disparo1_abajo.canm",
    "15A": "15A_habilidad_005_disparo2_abajo.canm",
    "15B": "15B_habilidad_005_bucle3_abajo.canm",
    "15C": "15C_habilidad_005_bucle4_abajo.canm",
    "15D": "15D_habilidad_005_salida_abajo.canm",
    "15E": "15E_habilidad_005_22.canm",
    "15F": "15F_habilidad_005_23.canm",
    "160": "160_habilidad_005_evento_1.canm",
    "161": "161_habilidad_005_evento_2.canm",
    "162": "162_habilidad_005_evento_3.canm",
    "163": "163_habilidad_005_evento_4.canm",
    "164": "164_habilidad_005_evento_5.canm",
    "165": "165_habilidad_005_enemigo_1.canm",
    "166": "166_habilidad_005_enemigo_2.canm",
    "167": "167_habilidad_005_enemigo_3.canm",
    "168": "168_habilidad_005_enemigo_4.canm",
    "169": "169_habilidad_005_enemigo_5.canm",
    "16A": "16A_habilidad_005_34.canm",
    "16B": "16B_habilidad_005_inicio.canm",
    "16C": "16C_choque_poder_1.canm",
    "16D": "16D_choque_poder_2.canm",
    "16E": "16E_choque_poder_3.canm",
    "16F": "16F_choque_poder_4.canm",
    "170": "170_choque_poder_5.canm",
    "171": "171_choque_poder_6.canm",
    "172": "172_choque_poder_derrota.canm",
    "173": "173_choque_embestida_entrada.canm",
    "174": "174_choque_embestida_bucle.canm",
    "175": "175_choque_embestida_ganar.canm",
    "176": "176_choque_embestida_perder.canm",
    "177": "177_transformacion_entrada.canm",
    "178": "178_transformacion_bucle.canm",
    "179": "179_transformacion_salida.canm",
    "17A": "17A_guardia_poderosa_entrada.canm",
    "17B": "17B_guardia_poderosa_bucle.canm",
    "17C": "17C_caida_atras.canm",
    "17D": "17D_caida_frente.canm",
    "17E": "17E_buscar_ki.canm",
    "17F": "17F_buscar_scouter.canm",
    "180": "180_intro_entrada.canm",
    "181": "181_intro_bucle.canm",
    "182": "182_victoria_entrada.canm",
    "183": "183_victoria_bucle.canm",
    "184": "184_derrota.canm",
    "185": "185_burla.canm",
    "186": "186_lanzamiento_gigante_entrada.canm",
    "187": "187_lanzamiento_gigante_bucle.canm",
    "188": "188_lanzamiento_gigante_evento.canm",
    "189": "189_lanzamiento_gigante_enemigo.canm",
    "18A": "18A_lanzamiento_gigante_salida.canm",
    "18B": "18B_volar_sin_volar.canm",
    "18C": "18C_salto_sin_volar.canm",
    "18D": "18D_cancelar_soplo_entrada.canm",
    "18E": "18E_cancelar_soplo_bucle.canm",
    "18F": "18F_detransformacion_entrada.canm",
    "190": "190_detransformacion_bucle.canm",
    "191": "191_detransformacion_salida.canm",
    "192": "192_volar_rapido_subida.canm",
    "193": "193_esquivar_sonico_entrada.canm",
    "194": "194_esquivar_sonico_bucle.canm",
    "195": "195_esquivar_sonico_salida.canm",
    "196": "196_sorprendido.canm",
    "197": "197_ataque_rayo_entrada.canm",
    "198": "198_ataque_rayo_salida.canm",
    "199": "199_ki_rapido_entrada.canm",
    "19A": "19A_ki_rapido_carga.canm",
    "19B": "19B_ki_rapido_bucle.canm",
    "19C": "19C_ki_rapido_salida.canm",
    "19D": "19D_reposo_bucle.canm",
    "19E": "19E_wii_01.canm",
    "19F": "19F_wii_02.canm",
    "1A0": "1A0_wii_03.canm",
    "1A1": "1A1_wii_04.canm",
    "1A2": "1A2_wii_05.canm",
    "1A3": "1A3_wii_06.canm",
    "1A4": "1A4_wii_07.canm",
    "1A5": "1A5_wii_08.canm",
    "1A6": "1A6_wii_09.canm",
    "1A7": "1A7_wii_10.canm",
    "1A8": "1A8_wii_11.canm",
    "1A9": "1A9_wii_12.canm",
    "1AA": "1AA_wii_13.canm",
    "1AB": "1AB_wii_14.canm",
    "1AC": "1AC_wii_15.canm",
    "1AD": "1AD_wii_16.canm",
    "1AE": "1AE_wii_17.canm",
    "1AF": "1AF_wii_18.canm",
    "1B0": "1B0_wii_19.canm",
    "1B1": "1B1_blank.canm",
    "1B2": "1B2_blank.canm",
    "1B3": "1B3_blank.canm",
    "1B4": "1B4_blank.canm",
    "1B5": "1B5_blank.canm",
    "1B6": "1B6_blank.canm",
    "1B7": "1B7_blank.canm",
}

ANIMATION_LIST_LABELS = [f"{code} - {name}" for code, name in ANIMATIONS.items()]

HEX_CONDITIONS = {
    "Esperar 10 segundos": "0000",
    "Esperar 15 segundos": "0001",
    "Esperar 20 segundos": "0002",
    "Esperar 25 segundos": "0003",
    "Esperar 30 segundos": "0004",
    "Esperar 35 segundos": "0005",
    "Esperar 40 segundos": "0006",
    "Esperar 45 segundos": "0007",
    "Esperar 50 segundos": "0008",
    "Esperar 55 segundos": "0009",
    "Esperar 60 segundos": "000a",
    "Esperar 70 segundos": "000b",
    "Esperar 80 segundos": "000c",
    "Esperar 90 segundos": "000d",
    "Esperar 100 segundos": "000e",
    "Esperar 120 segundos": "000f",
    "Esperar 140 segundos": "0010",
    "Esperar 160 segundos": "0011",
    "Esperar 180 segundos": "0012",
    "Realizar Normal Clash": "0014",
    "Realizar Aéreo Clash": "0015",
    "Perder 1 Health Bar": "0016",
    "Perder 2 barras de salud": "0017",
    "Perder 3 barras de salud": "0018",
    "Perder 4 barras de salud": "0019",
    "Perder 5 barras de salud": "001a",
    "Perder 6 barras de salud": "001b",
    "Perder 7 barras de salud": "001c",
    "Llenar las barras de Ki": "001d",
    "Alcanzar el máximo de reservas de ráfaga": "001e",
    "Entrar en modo MÁXIMO PODER": "001f",
    "Transformar/Destransformar/Fusiónar": "0020",
    "Burlarse": "0021",
    "Caer al suelo/agua": "0022",
    "Realizar 1st Blast 1": "0024",
    "Realizar 2nd Blast 1": "0025",
    "Realizar 1st Blast 2": "0026",
    "Realizar 2nd Blast 2": "0027",
    "Realizar Ultimate Blast": "0028",
    "Golpear con 1st Blast 1": "0029",
    "Golpear con 2nd Blast 1": "002a",
    "Golpear con 1st Blast 2": "002b",
    "Golpear con 2nd Blast 2": "002c",
    "Golpear con Ultimate Blast": "002d",
    "Bloquear 1st Blast 2": "002e",
    "Bloquear 2nd Blast 2": "002f",
    "Bloquear Ultimate Blast": "0030",
    "Realizar Dragon Homing": "0031",
    "Realizar Vanishing Attack": "0032",
    "Realizar Throw": "0033",
    "Realizar Hyper Smash": "0034",
    "Golpear con Charged Ki Blast": "0036",
    "Realizar Fully Charged Left Smash Attack": "0037",
    "Realizar Fully Charged Right Smash Attack": "0038",
    "Realizar Fully Charged Up Smash Attack": "0039",
    "Realizar Fully Charged Down Smash Attack": "003a",
    "Realizar Fully Charged Neutral Smash Attack": "003b",
    "Realizar First Attack!": "003c",
    "Realizar Rush Attack": "003d",
    "Realizar Dragon Smash": "003e",
    "Realizar Burst Meteo Finisher": "003f",
    "Realizar Dash Smash": "0040",
    "Realizar Teleport": "0041",
    "Realizar Z-Counter": "0042",
    "Realizar Guard Crush": "0043",
    "Realizar Sonic Sway": "0044",
    "Realizar Emergency Blaster Wave": "0045",
    "Ganar Beam Struggle": "0046",
    "Ganar Normal Clash": "0047",
    "Ganar por K.O.": "0048",
    "Ganar via Ring out": "0049",
    "Realizar Misc. Melee Attack": "004b",
    "Press R3": "0050",
    "Realizar Blast 1 Finish": "0052",
    "Realizar Blast 2 Finish": "0053",
    "Defeat all teammates": "0054",
    "Recibir un golpe": "0055",
    "Inmediato": "ffff",
}

HEX_EVENTS = {
    "[P1] Inicio de batalla (no hace nada)": "0000",
    "[P1] Fin de batalla (no hace nada)": "0001",
    "[P1] Aéreo Clash (0002)": "0002",
    "[P1] Destrucción del mapa": "0003",
    "[P1] Normal Clash": "0004",
    "[P1] Aéreo Clash (0005)": "0005",
    "[P1] Aéreo Clash (0006)": "0006",
    "[P1] Aéreo Clash (0007)": "0007",
    "[P1] Beam Struggle (P1 1st B2 vs COM 1st B2)": "0008",
    "[P1] Beam Struggle (P1 1st B2 vs COM 2nd B2)": "0009",
    "[P1] Beam Struggle (P1 2nd B2 vs COM 1st B2)": "000a",
    "[P1] Beam Struggle (P1 2nd B2 vs COM 2nd B2)": "000b",
    "[P1] Beam Struggle (Ultimate Blasts)": "000c",
    "[P1] DESCONOCIDO (000D)": "000d",
    "[P1] DESCONOCIDO (000E)": "000e",
    "[P1] DESCONOCIDO (000F)": "000f",
    "[P1] Cambiar con compañero #1": "0010",
    "[P1] Cambiar con compañero #2": "0011",
    "[P1] Cambiar con compañero #3": "0012",
    "[P1] Cambiar con compañero #4": "0013",
    "[P1] Cambiar con compañero #5": "0014",
    "[P1] Asignar transformación": "0015",
    "[P1] Asignar destransformación": "0016",
    "[P1] Asignar fusión": "0017",
    "[P1] Go to MAX POWER Mode": "0018",
    "[P1] Activar 1st Blast 1": "0019",
    "[P1] Activar 2nd Blast 1": "001a",
    "[P1] Activar 1st Blast 2": "001b",
    "[P1] Activar 2nd Blast 2": "001c",
    "[P1] Activar Ultimate Blast": "001d",
    "[CPU] Cambiar con compañero #1": "8011",
    "[CPU] Cambiar con compañero #2": "8012",
    "[CPU] Cambiar con compañero #3": "8013",
    "[CPU] Cambiar con compañero #4": "8014",
    "[CPU] Cambiar con compañero #5": "8015",
    "[CPU] Asignar transformación": "8016",
    "[CPU] Asignar destransformación": "8017",
    "[CPU] Asignar fusión": "8018",
    "[CPU] Go to MAX POWER Mode": "8019",
    "[CPU] Activar 1st Blast 1": "801a",
    "[CPU] Activar 2nd Blast 1": "801b",
    "[CPU] Activar 1st Blast 2": "801c",
    "[CPU] Activar 2nd Blast 2": "801d",
    "[CPU] Activar Ultimate Blast": "801e",
}

CHARACTERS_EVENTS = {
    "00": "Goku (Inicial)",
    "01": "Goku (Medio)",
    "02": "Goku (Medio) - Super Saiyajin",
    "03": "Goku (Final)",
    "04": "Goku (Final) - Super Saiyajin",
    "05": "Goku (Final) - Super Saiyajin2",
    "06": "Goku (Final) - Super Saiyajin3",
    "07": "Goku (GT)",
    "08": "Goku (GT) - Super Saiyajin",
    "09": "Goku (GT) - Super Saiyajin3",
    "0A": "Goku (GT) - Super Saiyajin4",
    "0B": "Pequeño Goku",
    "0C": "Ozaru",
    "0D": "Pequeño Gohan",
    "0E": "Adolescente Gohan",
    "0F": "Adolescente Gohan - Super Saiyajin",
    "10": "Adolescente Gohan - Super Saiyajin2",
    "11": "Adulto Gohan",
    "12": "Adulto Gohan - Super Saiyajin",
    "13": "Adulto Gohan - Super Saiyajin2",
    "14": "Gran Saiyaman",
    "15": "Ultimate Gohan",
    "16": "Piccolo (Inicial)",
    "17": "Piccolo (Final)",
    "18": "Nail",
    "19": "Krillin",
    "1A": "Yamcha",
    "1B": "Tien",
    "1C": "Chiaotzu",
    "1D": "Vegeta (Scouter)",
    "1E": "Ozaru Vegeta",
    "1F": "Vegeta",
    "20": "Vegeta - Super Saiyajin",
    "21": "Super Vegeta",
    "22": "Vegeta (segunda forma)",
    "23": "Vegeta (2nd) - Super Saiyajin",
    "24": "Vegeta (2nd) - Super Saiyajin2",
    "25": "Vegeta (Final) - Majin",
    "26": "Vegeta (2nd) - Super Saiyajin4",
    "27": "Trunks (Espada)",
    "28": "Trunks (Espada) - Super Saiyajin",
    "29": "Trunks",
    "2A": "Trunks - Super Saiyajin",
    "2B": "Super Trunks",
    "2C": "Pequeño Trunks",
    "2D": "Pequeño Trunks - Super Saiyajin",
    "2E": "Goten",
    "2F": "Goten - Super Saiyajin",
    "30": "Gotenks",
    "31": "Gotenks - Super Saiyajin",
    "32": "Gotenks - Super Saiyajin3",
    "33": "Vegito",
    "34": "Super Vegito",
    "35": "Super Gogeta",
    "36": "Gogeta - Super Saiyajin4",
    "37": "Hercule",
    "38": "Videl",
    "39": "Gran Saiyaman 2",
    "3A": "Supremo Kai",
    "3B": "Kibito Kai",
    "3C": "Yajirobe",
    "3D": "Pikkon",
    "3E": "Tapion",
    "3F": "Pan",
    "40": "Uub",
    "41": "Majuub",
    "42": "Maestro Roshi",
    "43": "Maestro Roshi - MÁXIMO PODER",
    "44": "Abuelo Gohan",
    "45": "Nam",
    "46": "Androide #8",
    "47": "King Vegeta",
    "48": "Ozaru King Vegeta",
    "49": "Bardock",
    "4A": "Ozaru Bardock",
    "4B": "Fasha",
    "4C": "Ozaru Fasha",
    "4D": "Raditz",
    "4E": "Ozaru Raditz",
    "4F": "Saibamen",
    "50": "Nappa",
    "51": "Ozaru Nappa",
    "52": "Zarbon",
    "53": "Zarbon - Post-transformación",
    "54": "Dodoria",
    "55": "Cui",
    "56": "Ginyu",
    "57": "Recoome",
    "58": "Burter",
    "59": "Jeice",
    "5A": "Guldo",
    "5B": "Frieza - 1.ª forma",
    "5C": "Frieza - 2.ª forma",
    "5D": "Frieza - 3.ª forma",
    "5E": "Frieza - Forma final",
    "5F": "Frieza - Máximo poder",
    "60": "Mecha Frieza",
    "61": "King Cold",
    "62": "Appule",
    "63": "Frieza Soldado",
    "64": "Androide #16",
    "65": "Androide #18",
    "66": "Androide #18",
    "67": "Androide #19",
    "68": "Dr. Gero",
    "69": "Cell - 1.ª forma",
    "70": "Cell - 2.ª forma",
    "6B": "Cell - Forma perfecta",
    "6C": "Cell - Perfecto",
    "6D": "Cell Jr.",
    "6E": "Babidi",
    "6F": "Rey Demonio Dabura",
    "70": "Majin Buu",
    "71": "Majin Buu (Mal puro)",
    "72": "Super Buu",
    "73": "Super Buu - Gotenks Abs",
    "74": "Super Buu - Gohan Abs",
    "75": "Pequeño Buu",
    "76": "Garlic Jr.",
    "77": "Super Garlic Jr.",
    "78": "Dr. Wheelo",
    "79": "Turles",
    "7A": "Ozaru Turles",
    "7B": "Slug",
    "7C": "Slug - Gigante",
    "7D": "Salza",
    "7E": "Cooler",
    "7F": "Cooler - Forma final",
    "80": "Meta-Cooler",
    "81": "Androide #13",
    "82": "Androide #13 - Fusión",
    "83": "Broly",
    "84": "Broly - Super Saiyajin",
    "85": "Broly - LSuper Saiyajin",
    "86": "Zangya",
    "87": "Bojack",
    "88": "Bojack - Máximo poder",
    "89": "Janemba",
    "8A": "Super Janemba",
    "8B": "Hirudegarn",
    "8C": "Baby Vegeta",
    "8D": "Super Baby 1",
    "8E": "Super Baby 2",
    "8F": "Ozaru Baby",
    "90": "Super 17",
    "91": "Nuova Shenron",
    "92": "Syn Shenron",
    "93": "Omega Shenron",
    "94": "General Tao",
    "95": "Cíborg Tao",
    "96": "General Blue",
    "97": "Devilman",
    "98": "Pilaf Máquina",
    "99": "Pilaf Máquina - Fusión",
    "9A": "Tambourine",
    "9B": "Rey Demonio Piccolo",
    "9C": "Arale",
    "9D": "Chi-Chi",
    "9E": "Spopovich",
    "9F": "Future Gohan",
    "A0": "Future Gohan - Super Saiyajin",
}

HEX_TO_LABEL_COND = {v.lower(): k for k, v in HEX_CONDITIONS.items()}
HEX_TO_LABEL_EVENT = {v.lower(): k for k, v in HEX_EVENTS.items()}
CHAR_LIST_LABELS = [
    f"{hex_code} - {name}" for hex_code, name in CHARACTERS_EVENTS.items()
]


def normalize_hex(hex_str, mapping):
  clean = re.sub(r"[^0-9a-fA-F]", "", hex_str).lower()
  if len(clean) > 4:
    clean = clean[-4:]
  if clean in mapping:
    return clean
  if len(clean) == 4:
    swapped = clean[2:] + clean[:2]
    if swapped in mapping:
      return swapped
  return clean


def is_char_event(ev_label):
  keywords = [
      "Cambiar con compañero",
      "Asignar transformación",
      "Asignar destransformación",
      "Asignar fusión",
  ]
  return any(kw in ev_label for kw in keywords)


# ============================================================================
# --- MÓDULO DE Z-ITEMS (inyectado desde DBZ_ZIT_EDITOR.py) ---
# Tabla de Z-Items, utilidades de búsqueda/parseo y gestor de líneas $zit,
# integrados aquí para dar soporte a la nueva pestaña "Z-Items" del editor.
# ============================================================================

ZITEMS_CSV_DATA = """dec,nombre
0,Ataque Arriba 1
1,Ataque Arriba 2
2,Ataque Arriba 3
3,Defensa Arriba 1
4,Defensa Arriba 2
5,Defensa Arriba 3
6,Poder Ki Arriba 1
7,Poder Ki Arriba 2
8,Poder Ki Arriba 3
9,Super Arriba 1
10,Super Arriba 2
11,Super Arriba 3
12,Ataque Arriba 2 y Defensa Abajo 1
13,Defensa Arriba 2 y Ataque Abajo 1
14,Poder Ki Arriba 2 y Super Abajo 1
15,Super Arriba 2 y Poder Abajo 1
16,Ataque Arriba 3 y Super Abajo 1
17,Defensa Arriba 3 y Ataque Abajo 2
18,Poder Ki Arriba 3 y Defensa Abajo 1
19,Super Arriba 3 y Poder Abajo 2
20,Ataque Arriba 3 y Defensa Abajo 2
21,Defensa Arriba 3 y Poder Ki Abajo 1
22,Poder Ki Arriba 3 y Super Abajo 2
23,Super Arriba 3 y Ataque Abajo 1
24,Vacío 1
25,Vacío 2
26,Vacío 3
27,Vacío 4
28,Vacío 5
29,Vacío 6
30,Vacío 7
31,Vacío 8
32,Vacío 9
33,Vacío 10
34,Vuelo
35,Liberar Poder Latente 1
36,Liberar Poder Latente 2
37,Liberar Poder Latente 3
38,Control de Ki
39,Maestría del Dragon Dash
40,Punto Alto
41,Esencia de la Vista
42,Linaje Guerrero
43,Halo
44,Sello Demoníaco
45,Golpe Satisfactorio
46,Corazón Activo
47,Espíritu de Lucha Indomable
48,Rompe Mentes
49,Poder Gigantesco
50,Espíritu de Lucha Creciente
51,Medidas Secretas
52,Prueba de Amistad
53,Habilidad Curativa de Dende
54,Vida Eterna
55,Tensión Arriba
56,Tensión Alta
57,Bendición del Agua
58,Control Espiritual
59,Amante de la Justicia
60,Ambiciones Malvadas
61,Corazón de Dragón
62,Latido de Dragón
63,Espíritu de Dragón
64,Confianza
65,Control de Batalla
66,Arte Secreto de Kibito
67,Amenaza Persistente
68,Maestro Milagroso
69,Habilidad Exquisita
70,Retorno Rápido
71,Presión Pesada
72,Liberar Ki
73,Poder de la Ira
74,Poder del Dragón
75,¡Energía Latente!
76,¡Espíritu de Lucha!
77,¡Indignación!
78,¡En Serio!
79,Odio hacia los Saiyans
80,Ráfaga de Ataques 1
81,Ráfaga de Ataques 2
82,Ráfaga de Ataques 3
83,Maestro de la Guardia
84,Espejismo
85,Voluntad del Guerrero
86,Orgullo Malvado
87,Guardia Perfecta
88,Sparking Plus
89,Estilo del Fuerte
90,Aura del Emperador
91,Sparking Milagroso
92,Salvador
93,Cuerpo Ligero
94,Cuerpo Poderoso
95,Cuerpo Definitivo
96,Aura Dracónica
97,Golpe Maestro
98,Ráfaga Maestra
99,Lanzamiento Maestro
100,Ataque Cargado
101,Ataque Rápido
102,Ruptura de Dragón
103,Aplastamiento de Dragón
104,Ruptura Evasiva
105,Embestida Evasiva
106,Maestro de Combos
107,Carga Rápida
108,Súper Sentidos
109,Anillo de Broly
110,Poder Namekiano
111,Poder de la Tierra
112,Poder Universal
113,Carga de Aura Azul
114,Carga de Aura Morada
115,Carga de Aura Amarilla
116,Carga de Aura Roja
117,Carga de Aura Verde
118,Carga de Aura Blanca
119,Carga de Aura Rosa
120,Carga de Aura Violeta
121,Carga de Aura Definitiva
122,Carga de Aura Definitiva 3
123,Carga de Aura Definitiva 4
124,Entrenamiento del Maestro Roshi
125,Entrenamiento del Rey Kai
126,Beso de #18
127,Bufanda de #17
128,Máquina Médica
129,Vacío 11
130,Vacío 12
131,Vacío 13
132,Vacío 14
133,Vacío 15
134,Vacío 16
135,Vacío 17
136,Apoyo de Launch
137,Tipo Goku
138,Tipo Vegeta
139,Tipo Gohan
140,Tipo Trunks
141,Tipo Piccolo
142,Tipo Krillin
143,Tipo Tien
144,Tipo Chiaotzu
145,Tipo Yajirobe
146,Tipo Freezer
147,Tipo Cell
148,Tipo Majin Buu
149,Tipo Broly
150,Tipo Ginyu
151,Tipo Recoome
152,Vacío 18
153,Vacío 19
154,Vacío 20
155,Vacío 21
156,Vacío 22
157,Vacío 23
158,Vacío 24
159,Vacío 25
160,Vacío 26
161,Vacío 27
162,Guerrero Definitivo 1
163,Guerrero Definitivo 2
164,Guerrero Definitivo 3
165,Guerrero Definitivo 4
166,Guerrero Definitivo 5
167,Guerrero Definitivo 6
168,Guerrero Definitivo 7
169,Guerrero Definitivo 8
170,Ataque -25
171,Ataque -24
172,Ataque -23
173,Ataque -22
174,Ataque -21
175,Ataque -20
176,Ataque -19
177,Ataque -18
178,Ataque -17
179,Ataque -16
180,Ataque -15
181,Ataque -14
182,Ataque -13
183,Ataque -12
184,Ataque -11
185,Ataque -10
186,Ataque -9
187,Ataque -8
188,Ataque -7
189,Ataque -6
190,Ataque -5
191,Ataque -4
192,Ataque -3
193,Ataque -2
194,Ataque -1
195,Ataque 0
196,Ataque +1
197,Ataque +2
198,Ataque +3
199,Ataque +4
200,Ataque +5
201,Ataque +6
202,Ataque +7
203,Ataque +8
204,Ataque +9
205,Ataque +10
206,Ataque +11
207,Ataque +12
208,Ataque +13
209,Ataque +14
210,Ataque +15
211,Ataque +16
212,Ataque +17
213,Ataque +18
214,Ataque +19
215,Ataque +20
216,Ataque +21
217,Ataque +22
218,Ataque +23
219,Ataque +24
220,Ataque +25
221,Ataque +26
222,Ataque +27
223,Ataque +28
224,Ataque +29
225,Ataque +30
226,Ataque +31
227,Ataque +32
228,Ataque +33
229,Ataque +34
230,Ataque +35
231,Ataque +32
232,Ataque +37
233,Ataque +38
234,Ataque +39
"""


def load_zitems_from_text(text):
  table = {}
  reader = csv.DictReader(io.StringIO(text))
  for row in reader:
    try:
      table[int(row["dec"])] = row["nombre"]
    except (KeyError, ValueError):
      continue
  return table


ZITEMS = load_zitems_from_text(ZITEMS_CSV_DATA)
EMPTY_ZIT_VALUE = 0x00000000

ZIT_PATTERN = re.compile(r"\$zit(\d+)\s*:\s*&([0-9A-Fa-f]+)")
ZIT_EVENT_PATTERN = re.compile(r"^\s*\$(EV_\w+)\s*:\s*<")
ZIT_ACTOR_BLOCK_PATTERN = re.compile(r"\$(?:actor|name)\s*:\s*\$(\w+)")


def lookup_zitem(value: int) -> str:
  if value == EMPTY_ZIT_VALUE:
    return "— (vacío / sin asignar)"
  if value in ZITEMS:
    return ZITEMS[value]
  return f"Desconocido (índice {value} fuera de la tabla)"


def parse_zit_value(text: str):
  t = text.strip()
  if t == "":
    raise ValueError("Valor vacío.")
  low = t.lower()
  if low in ("vacio", "vacío", "none", "-"):
    return EMPTY_ZIT_VALUE
  if t.startswith("&"):
    t = t[1:]
  if re.fullmatch(r"[0-9]+", t):
    val = int(t, 10)
  elif re.fullmatch(r"[0-9A-Fa-f]+", t):
    val = int(t, 16)
  else:
    raise ValueError(f"No se pudo interpretar el valor: {text!r}")
  if val < 0 or val > 0xFFFFFFFF:
    raise ValueError("El valor debe caber en 32 bits (0 a FFFFFFFF).")
  return val


class ZitLinesManager:
  """Gestor de campos $zit que opera sobre texto en memoria (self.file_content
  del editor de BT3), en lugar de un archivo propio como en la herramienta
  original. Permite normalizar, listar y editar los 8 $zit por bloque."""

  def __init__(self, text=""):
    self.set_text(text)

  def set_text(self, text):
    self.lines = text.splitlines(keepends=True) if text else []
    self.entries = []
    self._parse()

  def get_text(self):
    return "".join(self.lines)

  def normalize_all_lines(self):
    """Asegura que cada línea con zits tenga los 8 zits ordenados como:
    $zit8, $zit1..$zit7, rellenando con 00000000 y con 8 dígitos hex."""
    for line_idx, line in enumerate(self.lines):
      matches = list(ZIT_PATTERN.finditer(line))
      if not matches:
        continue

      zit_dict = {}
      for m in matches:
        zit_dict[int(m.group(1))] = m.group(2)

      order = [8, 1, 2, 3, 4, 5, 6, 7]
      complete_zit_data = []
      for num in order:
        val = zit_dict.get(num, "00000000")
        if len(val) < 8:
          val = val.zfill(8)
        complete_zit_data.append((num, val))

      ordered_str = " ".join(f"$zit{num}: &{val}" for num, val in complete_zit_data)

      cleaned = line
      for m in reversed(matches):
        cleaned = cleaned[:m.start()] + cleaned[m.end():]

      first_pos = matches[0].start()
      self.lines[line_idx] = cleaned[:first_pos] + " " + ordered_str + " " + cleaned[first_pos:]
      self.lines[line_idx] = re.sub(r"[ \t]+", " ", self.lines[line_idx]).replace(" }", "}").replace("{ ", "{")

    self._parse()

  def _parse(self):
    self.entries = []
    current_event = "(fuera de evento)"
    current_actor = "-"

    for line_idx, line in enumerate(self.lines):
      ev_match = ZIT_EVENT_PATTERN.match(line)
      if ev_match:
        current_event = ev_match.group(1)

      actor_matches = ZIT_ACTOR_BLOCK_PATTERN.findall(line)
      if actor_matches:
        current_actor = actor_matches[-1]

      for m in ZIT_PATTERN.finditer(line):
        field_idx = m.group(1)
        hex_val = m.group(2)
        start, end = m.span(2)
        dec_val = int(hex_val, 16)
        self.entries.append({
            "line_idx": line_idx,
            "start": start,
            "end": end,
            "width": len(hex_val),
            "evento": current_event,
            "actor": current_actor,
            "campo": f"zit{field_idx}",
            "hex": hex_val.upper(),
            "dec": dec_val,
            "nombre": lookup_zitem(dec_val),
        })

  def apply_edit(self, entry, new_dec: int):
    width = 8
    new_hex = format(new_dec, f"0{width}X")
    if len(new_hex) > width:
      width = len(new_hex)

    line_idx = entry["line_idx"]
    start, end = entry["start"], entry["end"]
    line = self.lines[line_idx]
    new_line = line[:start] + new_hex + line[end:]
    shift = len(new_hex) - (end - start)
    self.lines[line_idx] = new_line

    entry["hex"] = new_hex
    entry["dec"] = new_dec
    entry["nombre"] = lookup_zitem(new_dec)
    entry["end"] = start + len(new_hex)
    entry["width"] = width

    if shift:
      for other in self.entries:
        if other is entry:
          continue
        if other["line_idx"] == line_idx and other["start"] > start:
          other["start"] += shift
          other["end"] += shift


class ZitEditDialog(tk.Toplevel):
  """Cuadro de diálogo para editar un $zit concreto, con lista buscable de
  la tabla completa de Z-Items y campo manual para valores hex/dec."""

  def __init__(self, parent, entry, on_accept):
    super().__init__(parent)
    self.entry = entry
    self.on_accept = on_accept
    self.title(f"Editar {entry['campo']} — {entry['actor']} ({entry['evento']})")
    self.geometry("480x480")
    self.resizable(False, False)
    self.transient(parent)
    self.grab_set()

    info = (
        f"Evento: {entry['evento']}    Actor: {entry['actor']}    "
        f"Campo: {entry['campo']}\n"
        f"Valor actual: &{entry['hex']}  (dec {entry['dec']})  -> {entry['nombre']}"
    )
    ttk.Label(self, text=info, justify="left", wraplength=460).pack(
        fill="x", padx=10, pady=(10, 6)
    )

    ttk.Separator(self).pack(fill="x", padx=10, pady=4)

    ttk.Label(self, text="Buscar Z-Item en la lista:").pack(
        anchor="w", padx=10, pady=(6, 0)
    )
    self.search_var = tk.StringVar()
    self.search_var.trace_add("write", lambda *a: self._refresh_list())
    search_entry = ttk.Entry(self, textvariable=self.search_var)
    search_entry.pack(fill="x", padx=10, pady=(2, 6))

    list_frame = ttk.Frame(self)
    list_frame.pack(fill="both", expand=True, padx=10)
    self.listbox = tk.Listbox(list_frame, activestyle="dotbox")
    self.listbox.pack(side="left", fill="both", expand=True)
    sb = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
    self.listbox.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y")
    self.listbox.bind("<<ListboxSelect>>", self._on_select)
    self.listbox.bind("<Double-Button-1>", lambda e: self._accept())

    self._all_items = sorted(ZITEMS.items())
    self._visible_items = []
    self._refresh_list()

    ttk.Separator(self).pack(fill="x", padx=10, pady=6)

    manual_frame = ttk.Frame(self)
    manual_frame.pack(fill="x", padx=10, pady=(0, 6))
    ttk.Label(
        manual_frame,
        text="Valor manual (hex, decimal, o 'vacio' para &00000000):",
    ).pack(anchor="w")
    self.manual_var = tk.StringVar(value=f"&{entry['hex']}")
    ttk.Entry(manual_frame, textvariable=self.manual_var).pack(fill="x", pady=(2, 0))
    ttk.Label(
        manual_frame,
        text="Útil para valores fuera de la tabla o correcciones directas.",
        foreground="#666666",
    ).pack(anchor="w", pady=(2, 0))

    btns = ttk.Frame(self)
    btns.pack(fill="x", padx=10, pady=10)
    ttk.Button(btns, text="Cancelar", command=self.destroy).pack(side="right")
    ttk.Button(btns, text="Aceptar", command=self._accept).pack(side="right", padx=(0, 6))

  def _refresh_list(self):
    term = self.search_var.get().strip().lower()
    self.listbox.delete(0, "end")
    self._visible_items = []
    for dec, nombre in self._all_items:
      label = f"{dec:>3} - {nombre}"
      if term and term not in label.lower():
        continue
      self.listbox.insert("end", label)
      self._visible_items.append((dec, nombre))

  def _on_select(self, _event):
    sel = self.listbox.curselection()
    if not sel:
      return
    dec, _nombre = self._visible_items[sel[0]]
    self.manual_var.set(str(dec))

  def _accept(self):
    try:
      new_dec = parse_zit_value(self.manual_var.get())
    except ValueError as e:
      messagebox.showerror("Valor inválido", str(e), parent=self)
      return
    self.on_accept(new_dec)
    self.destroy()




# --------------------------------------------------------------------------
# Editor de posición/rotación ($Set_transform) - integrado desde
# BT3_position_editor.py
# --------------------------------------------------------------------------

POS_TRANSFORM_RE = re.compile(
    r"\$Set_transform:\{\$actor:\$(?P<actor>\w+)\s+"
    r"\$loc:F\[\s*(?P<lx>-?\d+\.\d+),\s*(?P<ly>-?\d+\.\d+),\s*(?P<lz>-?\d+\.\d+)\]\s+"
    r"\$rot:F\[\s*(?P<rx>-?\d+\.\d+),\s*(?P<ry>-?\d+\.\d+),\s*(?P<rz>-?\d+\.\d+)\]\}"
)

POS_ACTOR_COLORS = {
    "pla0": "#2E86FF", "pla1": "#4FB0FF", "pla2": "#8FD3FF",
    "cpu0": "#FF3B30", "cpu1": "#FF7A6E", "cpu2": "#FFAFA6",
}


def pos_color_for(actor):
  return POS_ACTOR_COLORS.get(actor, "#8A8A8A")


class PosTransform:
  """Representa una ocurrencia de $Set_transform en el archivo actual."""

  def __init__(self, event, actor, loc, rot, start, end):
    self.event = event
    self.actor = actor
    self.loc = list(loc)   # [x, y, z]
    self.rot = list(rot)   # [rx, ry, rz]
    self.start = start     # offset en self.file_content al momento del parseo
    self.end = end
    self.modified = False

  def label(self):
    return f"{self.event}  |  {self.actor}"

  def format(self):
    """Regenera el texto $Set_transform con los valores actuales."""
    x, y, z = self.loc
    rx, ry, rz = self.rot
    return (
        f"$Set_transform:{{$actor:${self.actor} "
        f"$loc:F[{x:.6f}, {y:.6f}, {z:.6f}] "
        f"$rot:F[{rx:.6f}, {ry:.6f}, {rz:.6f}]}}"
    )


def parse_pos_transforms(raw_text):
  """Encuentra todos los $Set_transform y a qué evento pertenece cada uno."""
  ev_matches = list(re.finditer(r'["\']?(\$EV_\w+|EV_\w+)["\']?', raw_text))

  def event_for_offset(offset):
    for ev_m in reversed(ev_matches):
      if ev_m.start() < offset:
        return ev_m.group(1).replace('"', "").replace("'", "")
    return "DESCONOCIDO"

  transforms = []
  for m in POS_TRANSFORM_RE.finditer(raw_text):
    loc = (float(m.group("lx")), float(m.group("ly")), float(m.group("lz")))
    rot = (float(m.group("rx")), float(m.group("ry")), float(m.group("rz")))
    ev = event_for_offset(m.start())
    transforms.append(PosTransform(ev, m.group("actor"), loc, rot, m.start(), m.end()))
  return transforms


# --------------------------------------------------------------------------
# Sistema de temas dinámicos / personalizables
# --------------------------------------------------------------------------

APP_COPYRIGHT = "© EpiDark-2026"
APP_CREDITS = ["Vras", "Furuya Dthem", "RidJuampa", "Vive"]


def _clamp8(v):
  return max(0, min(255, int(v)))


def _hex_to_rgb(h):
  h = h.lstrip("#")
  if len(h) == 3:
    h = "".join(c * 2 for c in h)
  return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _rgb_to_hex(rgb):
  return "#%02x%02x%02x" % tuple(_clamp8(c) for c in rgb)


def shade_hex(h, amount):
  """amount > 0 aclara, amount < 0 oscurece."""
  r, g, b = _hex_to_rgb(h)
  return _rgb_to_hex((r + amount, g + amount, b + amount))


def mix_hex(h1, h2, t):
  """Interpola entre dos colores hex (t entre 0 y 1)."""
  r1, g1, b1 = _hex_to_rgb(h1)
  r2, g2, b2 = _hex_to_rgb(h2)
  return _rgb_to_hex((
      r1 + (r2 - r1) * t,
      g1 + (g2 - g1) * t,
      b1 + (b2 - b1) * t,
  ))


THEME_PRESETS = {
    "Azul Boreal":    {"bg": "#10141a", "frame_bg": "#1a212c", "accent": "#2f8fef"},
    "Violeta Gala":   {"bg": "#150f1e", "frame_bg": "#20182e", "accent": "#a35cff"},
    "Esmeralda Namek": {"bg": "#0d1712", "frame_bg": "#15241d", "accent": "#2ecc8f"},
    "Carmesí Saiyan": {"bg": "#190f11", "frame_bg": "#241318", "accent": "#ff4757"},
    "Ámbar Kaio":     {"bg": "#191408", "frame_bg": "#251d0f", "accent": "#f5a623"},
}

DEFAULT_THEME_NAME = "Azul Boreal"


class BT3CombinedEditor:

  def __init__(self, root):
    self.root = root
    self.root.title("DBZ BT3 STORY MODE EDITOR")
    self.root.geometry("1120x780")

    self.file_path = None
    self.file_content = ""

    self.triggers_list = []
    self.events_list = []
    self.anims_list = []
    self.selected_trig_idx = None
    self.selected_ev_idx = None
    self.selected_anim_idx = None

    # --- estado del editor de posición/rotación ($Set_transform) ---
    self.pos_transforms = []
    self.pos_selected = None
    self.pos_clipboard = None
    self.pos_updating_fields = False

    # --- estado del tema visual (personalizable) ---
    self.theme_name = DEFAULT_THEME_NAME
    self.theme = dict(THEME_PRESETS[DEFAULT_THEME_NAME])

    self.setup_dark_theme()
    self.setup_background_image()

    self.menubar = tk.Menu(root)
    self.file_menu = tk.Menu(self.menubar, tearoff=0)
    self.file_menu.add_command(label="📁 Cargar Archivo", command=self.load_file)
    self.file_menu.add_command(label="💾 Guardar", command=self.save_file)
    self.file_menu.add_command(label="💾 Guardar como...", command=self.save_file_as)
    self.menubar.add_cascade(label="Archivo", menu=self.file_menu)

    self.appearance_menu = tk.Menu(self.menubar, tearoff=0)
    self.theme_preset_menu = tk.Menu(self.appearance_menu, tearoff=0)
    for preset_name in THEME_PRESETS:
      self.theme_preset_menu.add_command(
          label=preset_name,
          command=lambda n=preset_name: self.set_preset_theme(n),
      )
    self.appearance_menu.add_cascade(label="🎨 Temas predefinidos", menu=self.theme_preset_menu)
    self.appearance_menu.add_separator()
    self.appearance_menu.add_command(
        label="🖌 Color de acento personalizado...", command=self.choose_custom_accent
    )
    self.appearance_menu.add_command(
        label="🌑 Color de fondo personalizado...", command=self.choose_custom_background
    )
    self.appearance_menu.add_separator()
    self.appearance_menu.add_command(
        label="↺ Restablecer tema", command=self.reset_theme
    )
    self.menubar.add_cascade(label="Apariencia", menu=self.appearance_menu)

    self.help_menu = tk.Menu(self.menubar, tearoff=0)
    self.help_menu.add_command(label="ℹ️ Créditos", command=self.show_credits)
    self.menubar.add_cascade(label="Ayuda", menu=self.help_menu)

    root.config(menu=self.menubar)
    self.apply_theme_to_menus()

    # ---- barra superior: título de la app + acciones rápidas ----
    self.topbar = ttk.Frame(root, padding=(12, 8, 12, 4))
    self.topbar.pack(side="top", fill="x")

    self.app_title_label = ttk.Label(
        self.topbar, text="DBZ BT3 · STORY MODE EDITOR",
        font=("Segoe UI", 13, "bold"),
    )
    self.app_title_label.pack(side="left")

    self.lbl_file = ttk.Label(
        self.topbar, text="Sin archivo cargado",
        font=("Segoe UI", 9, "italic"), style="Muted.TLabel",
    )
    self.lbl_file.pack(side="left", padx=(16, 0))

    self.btn_credits = ttk.Button(
        self.topbar, text="ℹ️ Créditos", command=self.show_credits
    )
    self.btn_credits.pack(side="right")

    self.btn_theme = ttk.Button(
        self.topbar, text="🎨 Personalizar tema", command=self.open_theme_picker
    )
    self.btn_theme.pack(side="right", padx=(0, 6))

    # ---- barra inferior: copyright ----
    self.footer = ttk.Frame(root, padding=(12, 4, 12, 6))
    self.footer.pack(side="bottom", fill="x")

    self.lbl_copyright = ttk.Label(
        self.footer, text=APP_COPYRIGHT, style="Muted.TLabel", font=("Segoe UI", 8, "italic")
    )
    self.lbl_copyright.pack(side="right")

    self.main_notebook = ttk.Notebook(root)
    self.main_notebook.pack(fill="both", expand=True, padx=10, pady=5)

    self.zit_manager = ZitLinesManager("")
    self.zit_row_to_entry = {}

    self.tab_main_editor = ttk.Frame(self.main_notebook)
    self.tab_stats_editor = ttk.Frame(self.main_notebook)
    self.tab_events_editor = ttk.Frame(self.main_notebook)
    self.tab_anim_editor = ttk.Frame(self.main_notebook)
    self.tab_zit_editor = ttk.Frame(self.main_notebook)
    self.tab_position_editor = ttk.Frame(self.main_notebook)

    self.main_notebook.add(
        self.tab_main_editor, text=" Personajes y Ajustes "
    )
    self.main_notebook.add(self.tab_stats_editor, text=" Salud e IA ")
    self.main_notebook.add(
        self.tab_events_editor, text=" Eventos y Condicionales "
    )
    self.main_notebook.add(
        self.tab_anim_editor, text=" Anim "
    )
    self.main_notebook.add(
        self.tab_zit_editor, text=" Z-Items "
    )
    self.main_notebook.add(
        self.tab_position_editor, text=" Posición/Rotación "
    )

    self.setup_story_editor_ui(self.tab_main_editor)
    self.setup_stats_editor_ui(self.tab_stats_editor)
    self.setup_events_editor_ui(self.tab_events_editor)
    self.setup_anim_editor_ui(self.tab_anim_editor)
    self.setup_zit_editor_ui(self.tab_zit_editor)
    self.setup_position_editor_ui(self.tab_position_editor)

  def setup_dark_theme(self):
    self.apply_theme()

  def apply_theme(self):
    """(Re)aplica el tema actual (self.theme) a todos los estilos ttk
    y a los widgets tk "crudos" que no siguen ttk.Style automáticamente."""
    th = self.theme
    bg_color = th["bg"]
    frame_bg = th["frame_bg"]
    accent_color = th["accent"]
    fg_color = "#f3f3f3"
    muted_fg = shade_hex(bg_color, 120)
    field_bg = shade_hex(frame_bg, 12)
    hover = shade_hex(accent_color, 22)
    pressed = shade_hex(accent_color, -22)
    header_bg = shade_hex(frame_bg, -8)

    style = ttk.Style()
    style.theme_use("clam")

    self.root.configure(bg=bg_color)

    style.configure(".", background=bg_color, foreground=fg_color, font=("Segoe UI", 10))
    style.configure("TLabel", background=bg_color, foreground=fg_color)
    style.configure("Muted.TLabel", background=bg_color, foreground=muted_fg)
    style.configure(
        "TLabelframe", background=frame_bg, foreground=fg_color, borderwidth=1
    )
    style.configure(
        "TLabelframe.Label", background=frame_bg, foreground=accent_color,
        font=("Segoe UI", 10, "bold"),
    )
    style.configure("TFrame", background=bg_color)
    style.configure(
        "TButton", background=field_bg, foreground=fg_color, borderwidth=1,
        padding=6, focuscolor=accent_color,
    )
    style.map(
        "TButton",
        background=[("active", hover), ("pressed", pressed)],
        foreground=[("active", "#ffffff"), ("pressed", "#ffffff")],
    )
    style.configure(
        "TCheckbutton", background=bg_color, foreground=fg_color,
    )
    style.map(
        "TCheckbutton",
        background=[("active", bg_color)],
        indicatorbackground=[("selected", accent_color)],
    )
    style.configure(
        "TCombobox", fieldbackground=field_bg, background=field_bg, foreground=fg_color,
        arrowcolor=accent_color,
    )
    style.map(
        "TCombobox",
        fieldbackground=[("readonly", field_bg)],
        selectbackground=[("readonly", accent_color)],
        selectforeground=[("readonly", "#ffffff")],
    )
    style.configure(
        "TEntry", fieldbackground=field_bg, foreground=fg_color, insertcolor=accent_color,
    )
    style.configure(
        "Horizontal.TScale", background=bg_color, troughcolor=field_bg,
    )
    style.configure(
        "TScrollbar", background=field_bg, troughcolor=bg_color, arrowcolor=accent_color,
    )
    style.configure("TNotebook", background=bg_color, borderwidth=0)
    style.configure(
        "TNotebook.Tab", background=header_bg, foreground=muted_fg,
        padding=[12, 6], font=("Segoe UI", 9, "bold"),
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", accent_color), ("active", hover)],
        foreground=[("selected", "#ffffff"), ("active", "#ffffff")],
    )
    style.configure(
        "Treeview",
        background=frame_bg,
        foreground=fg_color,
        fieldbackground=frame_bg,
        rowheight=25,
    )
    style.configure(
        "Treeview.Heading", background=header_bg, foreground=accent_color, borderwidth=1
    )
    style.map(
        "Treeview",
        background=[("selected", accent_color)],
        foreground=[("selected", "#ffffff")],
    )

    # widgets tk "crudos" que no se pintan solos con ttk.Style
    if hasattr(self, "pos_canvas"):
      self.pos_canvas.configure(bg=shade_hex(bg_color, -6))
    if hasattr(self, "pos_listbox"):
      self.pos_listbox.configure(
          bg=field_bg, fg=fg_color, selectbackground=accent_color,
          selectforeground="#ffffff", highlightthickness=0, relief="flat",
      )
    if hasattr(self, "canvas"):
      self.canvas.configure(bg=shade_hex(bg_color, -6))

    self.apply_theme_to_menus()

  def apply_theme_to_menus(self):
    """Colorea los tk.Menu (Archivo/Apariencia/Ayuda), que no siguen ttk.Style."""
    th = self.theme
    menu_bg = shade_hex(th["frame_bg"], -6)
    menu_fg = "#f3f3f3"
    menu_active = th["accent"]
    for m in (
        getattr(self, "menubar", None),
        getattr(self, "file_menu", None),
        getattr(self, "appearance_menu", None),
        getattr(self, "theme_preset_menu", None),
        getattr(self, "help_menu", None),
    ):
      if m is None:
        continue
      try:
        m.configure(
            bg=menu_bg, fg=menu_fg,
            activebackground=menu_active, activeforeground="#ffffff",
        )
      except tk.TclError:
        pass

  # ------------------------------------------------------- personalización --
  def set_preset_theme(self, name):
    if name not in THEME_PRESETS:
      return
    self.theme_name = name
    self.theme = dict(THEME_PRESETS[name])
    self.apply_theme()

  def choose_custom_accent(self):
    _, hex_color = colorchooser.askcolor(
        color=self.theme["accent"], title="Elige el color de acento",
        parent=self.root,
    )
    if hex_color:
      self.theme["accent"] = hex_color
      self.theme_name = "Personalizado"
      self.apply_theme()

  def choose_custom_background(self):
    _, hex_color = colorchooser.askcolor(
        color=self.theme["bg"], title="Elige el color de fondo",
        parent=self.root,
    )
    if hex_color:
      self.theme["bg"] = hex_color
      self.theme["frame_bg"] = shade_hex(hex_color, 12)
      self.theme_name = "Personalizado"
      self.apply_theme()

  def reset_theme(self):
    self.set_preset_theme(DEFAULT_THEME_NAME)

  def open_theme_picker(self):
    win = tk.Toplevel(self.root)
    win.title("Personalizar tema")
    win.resizable(False, False)
    win.transient(self.root)
    win.configure(bg=self.theme["bg"])

    pad = ttk.Frame(win, padding=16)
    pad.pack(fill="both", expand=True)

    ttk.Label(
        pad, text="Elige un tema o personaliza tus propios colores",
        font=("Segoe UI", 10, "bold"),
    ).pack(anchor="w", pady=(0, 10))

    presets_frame = ttk.Frame(pad)
    presets_frame.pack(fill="x")
    for name, colors in THEME_PRESETS.items():
      swatch = tk.Button(
          presets_frame, text=name, bg=colors["accent"], fg="#ffffff",
          activebackground=shade_hex(colors["accent"], 20), relief="flat",
          borderwidth=0, padx=10, pady=6,
          command=lambda n=name: (self.set_preset_theme(n), win.destroy()),
      )
      swatch.pack(fill="x", pady=3)

    ttk.Separator(pad, orient="horizontal").pack(fill="x", pady=10)

    ttk.Button(
        pad, text="🖌 Color de acento personalizado...",
        command=lambda: (self.choose_custom_accent(), win.destroy()),
    ).pack(fill="x", pady=3)
    ttk.Button(
        pad, text="🌑 Color de fondo personalizado...",
        command=lambda: (self.choose_custom_background(), win.destroy()),
    ).pack(fill="x", pady=3)
    ttk.Button(
        pad, text="↺ Restablecer tema por defecto",
        command=lambda: (self.reset_theme(), win.destroy()),
    ).pack(fill="x", pady=(10, 0))

    ttk.Button(pad, text="Cerrar", command=win.destroy).pack(fill="x", pady=(14, 0))

    win.update_idletasks()
    rx, ry = self.root.winfo_rootx(), self.root.winfo_rooty()
    rw, rh = self.root.winfo_width(), self.root.winfo_height()
    ww, wh = win.winfo_width(), win.winfo_height()
    win.geometry(f"+{rx + (rw - ww) // 2}+{ry + (rh - wh) // 2}")

  # ------------------------------------------------------------ créditos --
  def show_credits(self):
    win = tk.Toplevel(self.root)
    win.title("Créditos")
    win.resizable(False, False)
    win.transient(self.root)
    win.configure(bg=self.theme["bg"])
    win.grab_set()

    pad = ttk.Frame(win, padding=(24, 20, 24, 16))
    pad.pack(fill="both", expand=True)

    ttk.Label(pad, text="Créditos:", font=("Segoe UI", 12, "bold")).pack(anchor="w")

    names_frame = ttk.Frame(pad, padding=(4, 8, 4, 4))
    names_frame.pack(fill="x")
    for name in APP_CREDITS:
      ttk.Label(names_frame, text=name, font=("Segoe UI", 10)).pack(anchor="w", pady=1)

    ttk.Separator(pad, orient="horizontal").pack(fill="x", pady=(10, 8))
    ttk.Label(pad, text=APP_COPYRIGHT, style="Muted.TLabel", font=("Segoe UI", 8, "italic")).pack(anchor="e")

    ttk.Button(pad, text="Cerrar", command=win.destroy).pack(fill="x", pady=(14, 0))

    win.update_idletasks()
    rx, ry = self.root.winfo_rootx(), self.root.winfo_rooty()
    rw, rh = self.root.winfo_width(), self.root.winfo_height()
    ww, wh = win.winfo_width(), win.winfo_height()
    win.geometry(f"+{rx + (rw - ww) // 2}+{ry + (rh - wh) // 2}")

  def setup_background_image(self):
    image_name = "background.png"
    if os.path.exists(image_name):
      try:
        self.bg_image = tk.PhotoImage(file=image_name)
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.lower()
      except Exception as e:
        print(f"No se pudo cargar la imagen PNG: {e}")

  def setup_story_editor_ui(self, parent):
    frame_settings = ttk.LabelFrame(parent, text=" Escenario y Música ")
    frame_settings.pack(fill="x", padx=10, pady=5)

    ttk.Label(frame_settings, text="Mapa ($map):").grid(
        row=0, column=0, sticky="w", padx=5, pady=5
    )
    self.cmb_map = ttk.Combobox(
        frame_settings, values=list(MAPS.values()), state="readonly", width=50
    )
    self.cmb_map.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_settings, text="Música ($bgm):").grid(
        row=1, column=0, sticky="w", padx=5, pady=5
    )
    self.cmb_bgm = ttk.Combobox(
        frame_settings, values=list(BGMS.values()), state="readonly", width=50
    )
    self.cmb_bgm.grid(row=1, column=1, padx=5, pady=5)

    self.notebook_teams = ttk.Notebook(parent)
    self.notebook_teams.pack(fill="both", expand=True, padx=10, pady=5)

    self.tab_players = ttk.Frame(self.notebook_teams)
    self.tab_cpus = ttk.Frame(self.notebook_teams)

    self.notebook_teams.add(self.tab_players, text=" Equipo Jugador ")
    self.notebook_teams.add(self.tab_cpus, text=" Equipo Rival CPU ")

    self.init_characters_tabs()

  def init_characters_tabs(self):
    self.cmb_players, self.cmb_player_costumes, self.chk_player_dmg = [], [], []
    self.cmb_cpus, self.cmb_cpu_costumes, self.chk_cpu_dmg = [], [], []

    for i in range(5):
      lbl_text = "Líder (pla0):" if i == 0 else f"Compañero {i} (pla{i}):"
      ttk.Label(self.tab_players, text=lbl_text).grid(
          row=i, column=0, sticky="w", padx=10, pady=8
      )
      vals = (
          list(CHARACTERS_STORY.values())
          if i == 0
          else [EMPTY_SLOT] + list(CHARACTERS_STORY.values())
      )
      cmb_char = ttk.Combobox(
          self.tab_players, values=vals, state="readonly", width=32
      )
      cmb_char.grid(row=i, column=1, padx=5, pady=8)
      cmb_char.set(vals[0])
      self.cmb_players.append(cmb_char)

      cmb_cost = ttk.Combobox(
          self.tab_players,
          values=list(COSTUMES.values()),
          state="readonly",
          width=12,
      )
      cmb_cost.grid(row=i, column=2, padx=5, pady=8)
      cmb_cost.set(COSTUMES["0"])
      self.cmb_player_costumes.append(cmb_cost)

      var_dmg = tk.IntVar(value=0)
      chk_dmg = ttk.Checkbutton(
          self.tab_players, text="Dañado ($dmg)", variable=var_dmg
      )
      chk_dmg.grid(row=i, column=3, padx=5, pady=8)
      self.chk_player_dmg.append(var_dmg)

    for i in range(5):
      lbl_text = "Líder CPU (cpu0):" if i == 0 else f"Compañero {i} (cpu{i}):"
      ttk.Label(self.tab_cpus, text=lbl_text).grid(
          row=i, column=0, sticky="w", padx=10, pady=8
      )
      vals = (
          list(CHARACTERS_STORY.values())
          if i == 0
          else [EMPTY_SLOT] + list(CHARACTERS_STORY.values())
      )
      cmb_char = ttk.Combobox(
          self.tab_cpus, values=vals, state="readonly", width=32
      )
      cmb_char.grid(row=i, column=1, padx=5, pady=8)
      cmb_char.set(vals[0])
      self.cmb_cpus.append(cmb_char)

      cmb_cost = ttk.Combobox(
          self.tab_cpus,
          values=list(COSTUMES.values()),
          state="readonly",
          width=12,
      )
      cmb_cost.grid(row=i, column=2, padx=5, pady=8)
      cmb_cost.set(COSTUMES["0"])
      self.cmb_cpu_costumes.append(cmb_cost)

      var_dmg = tk.IntVar(value=0)
      chk_dmg = ttk.Checkbutton(
          self.tab_cpus, text="Dañado ($dmg)", variable=var_dmg
      )
      chk_dmg.grid(row=i, column=3, padx=5, pady=8)
      self.chk_cpu_dmg.append(var_dmg)

  def setup_stats_editor_ui(self, parent):
    frame_info = ttk.LabelFrame(
        parent, text=" Configuración de Salud e Inteligencia Artificial "
    )
    frame_info.pack(fill="both", expand=True, padx=10, pady=10)

    notebook_stats = ttk.Notebook(frame_info)
    notebook_stats.pack(fill="both", expand=True, padx=5, pady=5)

    tab_p_stats = ttk.Frame(notebook_stats)
    tab_c_stats = ttk.Frame(notebook_stats)

    notebook_stats.add(tab_p_stats, text=" Jugadores ($hp / $ia) ")
    notebook_stats.add(tab_c_stats, text=" CPU ($hp / $ia) ")

    self.ent_player_hp, self.ent_player_ia = [], []
    self.ent_cpu_hp, self.ent_cpu_ia = [], []

    for i in range(5):
      lbl = "Líder (pla0):" if i == 0 else f"Compañero {i} (pla{i}):"
      ttk.Label(tab_p_stats, text=lbl).grid(
          row=i, column=0, sticky="w", padx=10, pady=10
      )
      ttk.Label(tab_p_stats, text="Salud ($hp):").grid(
          row=i, column=1, padx=5, pady=10
      )
      ent_hp = ttk.Entry(tab_p_stats, width=12)
      ent_hp.insert(0, "30000")
      ent_hp.grid(row=i, column=2, padx=5, pady=10)
      self.ent_player_hp.append(ent_hp)

      ttk.Label(tab_p_stats, text="Nivel IA ($ia):").grid(
          row=i, column=3, padx=5, pady=10
      )
      ent_ia = ttk.Entry(tab_p_stats, width=12)
      ent_ia.insert(0, "0")
      ent_ia.grid(row=i, column=4, padx=5, pady=10)
      self.ent_player_ia.append(ent_ia)

    for i in range(5):
      lbl = "Líder CPU (cpu0):" if i == 0 else f"Compañero {i} (cpu{i}):"
      ttk.Label(tab_c_stats, text=lbl).grid(
          row=i, column=0, sticky="w", padx=10, pady=10
      )
      ttk.Label(tab_c_stats, text="Salud ($hp):").grid(
          row=i, column=1, padx=5, pady=10
      )
      ent_hp = ttk.Entry(tab_c_stats, width=12)
      ent_hp.insert(0, "30000")
      ent_hp.grid(row=i, column=2, padx=5, pady=10)
      self.ent_cpu_hp.append(ent_hp)

      ttk.Label(tab_c_stats, text="Nivel IA ($ia):").grid(
          row=i, column=3, padx=5, pady=10
      )
      ent_ia = ttk.Entry(tab_c_stats, width=12)
      ent_ia.insert(0, "9")
      ent_ia.grid(row=i, column=4, padx=5, pady=10)
      self.ent_cpu_ia.append(ent_ia)

  def setup_events_editor_ui(self, parent):
    self.notebook_events = ttk.Notebook(parent)
    self.notebook_events.pack(fill="both", expand=True, padx=5, pady=5)

    self.tab_triggers = ttk.Frame(self.notebook_events)
    self.tab_events = ttk.Frame(self.notebook_events)

    self.notebook_events.add(
        self.tab_triggers, text=" Desencadenadores ($if) "
    )
    self.notebook_events.add(self.tab_events, text=" Lista de Eventos ($evt) ")

    self.setup_triggers_tab()
    self.setup_events_tab()

  def setup_triggers_tab(self):
    frame_top = ttk.LabelFrame(
        self.tab_triggers, text=" Modificar Desencadenador Seleccionado "
    )
    frame_top.pack(fill="x", padx=5, pady=5)

    ttk.Label(frame_top, text="Evento Padre:").grid(
        row=0, column=0, padx=5, pady=5
    )
    self.ent_trig_id = ttk.Entry(frame_top, width=15, state="readonly")
    self.ent_trig_id.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_top, text="Nueva Condición ($if):").grid(
        row=0, column=2, padx=5, pady=5
    )
    self.cmb_trig_cond = ttk.Combobox(
        frame_top, values=list(HEX_CONDITIONS.keys()), width=35
    )
    self.cmb_trig_cond.current(0)
    self.cmb_trig_cond.grid(row=0, column=3, padx=5, pady=5)

    ttk.Label(frame_top, text="Nuevo Ir a ($to):").grid(
        row=1, column=0, padx=5, pady=5
    )
    self.ent_trig_target = ttk.Entry(frame_top, width=15)
    self.ent_trig_target.grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(
        frame_top,
        text="🔄 Aplicar Cambio a Desencadenador",
        command=self.replace_trigger,
    ).grid(row=1, column=2, columnspan=2, pady=5)

    self.tree_triggers = ttk.Treeview(
        self.tab_triggers,
        columns=("ID", "Condicion_Hex", "Descripcion", "Destino"),
        show="headings",
    )
    self.tree_triggers.heading("ID", text="Evento Padre")
    self.tree_triggers.heading("Condicion_Hex", text="Hex ($if)")
    self.tree_triggers.heading("Descripcion", text="Desencadenador / Condición")
    self.tree_triggers.heading("Destino", text="Siguiente Evento ($to)")

    self.tree_triggers.column("ID", width=120)
    self.tree_triggers.column("Condicion_Hex", width=100)
    self.tree_triggers.column("Descripcion", width=360)
    self.tree_triggers.column("Destino", width=140)

    self.tree_triggers.pack(fill="both", expand=True, padx=5, pady=5)
    self.tree_triggers.bind("<<TreeviewSelect>>", self.on_trig_select)

  def setup_events_tab(self):
    frame_top = ttk.LabelFrame(
        self.tab_events, text=" Modificar Evento Seleccionado "
    )
    frame_top.pack(fill="x", padx=5, pady=5)

    ttk.Label(frame_top, text="Evento Padre:").grid(
        row=0, column=0, padx=2, pady=5
    )
    self.ent_ev_id = ttk.Entry(frame_top, width=12, state="readonly")
    self.ent_ev_id.grid(row=0, column=1, padx=2, pady=5)

    ttk.Label(frame_top, text="Evento ($evt):").grid(
        row=0, column=2, padx=2, pady=5
    )
    self.cmb_ev_select = ttk.Combobox(
        frame_top, values=list(HEX_EVENTS.keys()), width=42
    )
    self.cmb_ev_select.current(0)
    self.cmb_ev_select.grid(row=0, column=3, padx=2, pady=5)
    self.cmb_ev_select.bind("<<ComboboxSelected>>", self.on_evt_combo_change)

    ttk.Label(frame_top, text="Personaje ($flag):").grid(
        row=0, column=4, padx=2, pady=5
    )
    self.cmb_char_select = ttk.Combobox(
        frame_top, values=CHAR_LIST_LABELS, width=32, state="disabled"
    )
    self.cmb_char_select.current(0)
    self.cmb_char_select.grid(row=0, column=5, padx=2, pady=5)

    ttk.Button(
        frame_top,
        text="🔄 Aplicar Cambio a Evento",
        command=self.replace_event,
    ).grid(row=1, column=0, columnspan=6, pady=5)

    self.tree_events = ttk.Treeview(
        self.tab_events,
        columns=("Padre", "Hex_Actual", "Descripcion", "Flag_Hex", "Personaje"),
        show="headings",
    )
    self.tree_events.heading("Padre", text="Evento Padre")
    self.tree_events.heading("Hex_Actual", text="Hex ($evt)")
    self.tree_events.heading("Descripcion", text="Evento Ejecutado")
    self.tree_events.heading("Flag_Hex", text="Hex ($flag)")
    self.tree_events.heading("Personaje", text="Personaje Seleccionado")

    self.tree_events.column("Padre", width=110)
    self.tree_events.column("Hex_Actual", width=80)
    self.tree_events.column("Descripcion", width=340)
    self.tree_events.column("Flag_Hex", width=100)
    self.tree_events.column("Personaje", width=220)

    self.tree_events.pack(fill="both", expand=True, padx=5, pady=5)
    self.tree_events.bind("<<TreeviewSelect>>", self.on_ev_select)

  def setup_anim_editor_ui(self, parent):
    frame_top = ttk.LabelFrame(
        parent, text=" Modificar Animación Seleccionada ($Load_Anim) "
    )
    frame_top.pack(fill="x", padx=5, pady=5)

    ttk.Label(frame_top, text="Evento Padre:").grid(
        row=0, column=0, padx=5, pady=5, sticky="w"
    )
    self.ent_anim_id = ttk.Entry(frame_top, width=15, state="readonly")
    self.ent_anim_id.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_top, text="Actor ($actor):").grid(
        row=0, column=2, padx=5, pady=5, sticky="w"
    )
    self.ent_anim_actor = ttk.Entry(frame_top, width=15, state="readonly")
    self.ent_anim_actor.grid(row=0, column=3, padx=5, pady=5)

    ttk.Label(frame_top, text="Nueva Animación ($anm):").grid(
        row=1, column=0, padx=5, pady=5, sticky="w"
    )
    self.cmb_anim_select = ttk.Combobox(
        frame_top, values=ANIMATION_LIST_LABELS, width=45, state="readonly"
    )
    self.cmb_anim_select.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

    ttk.Label(frame_top, text="Ejecución ($Loop/$Wait):").grid(
        row=2, column=0, padx=5, pady=5, sticky="w"
    )
    self.cmb_anim_mode = ttk.Combobox(
        frame_top, values=["", "$Loop", "$Wait"], width=15, state="readonly"
    )
    self.cmb_anim_mode.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    ttk.Button(
        frame_top,
        text="🔄 Aplicar Cambio a Animación",
        command=self.replace_animation,
    ).grid(row=3, column=0, columnspan=4, pady=8)

    self.tree_anims = ttk.Treeview(
        parent,
        columns=("Padre", "Actor", "Anm_Hex", "Tipo_Animacion", "Modo"),
        show="headings",
    )
    self.tree_anims.heading("Padre", text="Evento Padre")
    self.tree_anims.heading("Actor", text="Actor ($actor)")
    self.tree_anims.heading("Anm_Hex", text="Hex ($anm)")
    self.tree_anims.heading("Tipo_Animacion", text="Nombre / Tipo de Animación")
    self.tree_anims.heading("Modo", text="Modo ($Loop/$Wait)")

    self.tree_anims.column("Padre", width=110)
    self.tree_anims.column("Actor", width=110)
    self.tree_anims.column("Anm_Hex", width=80)
    self.tree_anims.column("Tipo_Animacion", width=340)
    self.tree_anims.column("Modo", width=110)

    self.tree_anims.pack(fill="both", expand=True, padx=5, pady=5)
    self.tree_anims.bind("<<TreeviewSelect>>", self.on_anim_select)

  def setup_zit_editor_ui(self, parent):
    sub_notebook = ttk.Notebook(parent)
    sub_notebook.pack(fill="both", expand=True, padx=5, pady=5)

    self.zit_tab = ttk.Frame(sub_notebook)
    self.zit_comp_tab = ttk.Frame(sub_notebook)
    sub_notebook.add(self.zit_tab, text=" Editor de Z-Items ")
    sub_notebook.add(self.zit_comp_tab, text=" Comparar Archivos ")

    top_bar = ttk.Frame(self.zit_tab)
    top_bar.pack(fill="x", padx=8, pady=(8, 2))

    ttk.Label(
        top_bar,
        text="Los Z-Items se leen y se guardan junto con el resto del archivo cargado en 'Archivo'.",
        anchor="w",
    ).pack(side="left", fill="x", expand=True)

    ttk.Button(
        top_bar, text="Normalizar Z-Items", command=self.normalize_zits
    ).pack(side="right")
    ttk.Button(
        top_bar, text="Actualizar tabla", command=self.refresh_zit_table
    ).pack(side="right", padx=(0, 6))

    filter_bar = ttk.Frame(self.zit_tab)
    filter_bar.pack(fill="x", padx=8, pady=(0, 4))
    ttk.Label(filter_bar, text="Filtrar:").pack(side="left")
    self.zit_filter_var = tk.StringVar()
    self.zit_filter_var.trace_add("write", lambda *a: self.apply_zit_filter())
    ttk.Entry(filter_bar, textvariable=self.zit_filter_var).pack(
        side="left", fill="x", expand=True, padx=(4, 0)
    )

    hint = ttk.Label(
        self.zit_tab,
        text="Doble clic sobre una fila para cambiar su Z-Item. Orden al normalizar: $zit8, $zit1..$zit7 (Vacíos: &00000000).",
        foreground="#999999",
    )
    hint.pack(anchor="w", padx=8)

    columns = ("evento", "actor", "campo", "hex", "dec", "nombre")
    headers = {
        "evento": "Evento", "actor": "Actor", "campo": "Campo",
        "hex": "Valor (hex)", "dec": "Valor (dec)", "nombre": "Z-Item",
    }
    widths = {"evento": 100, "actor": 80, "campo": 60, "hex": 110, "dec": 90, "nombre": 380}

    table_frame = ttk.Frame(self.zit_tab)
    table_frame.pack(fill="both", expand=True, padx=8, pady=4)

    self.zit_tree = ttk.Treeview(table_frame, columns=columns, show="headings")
    for c in columns:
      self.zit_tree.heading(c, text=headers[c], command=lambda col=c: self.sort_zit_by(col))
      self.zit_tree.column(c, width=widths[c], anchor="w")
    self.zit_tree.pack(side="left", fill="both", expand=True)
    self.zit_tree.bind("<Double-1>", lambda e: self.edit_selected_zit())

    zit_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.zit_tree.yview)
    self.zit_tree.configure(yscroll=zit_scrollbar.set)
    zit_scrollbar.pack(side="right", fill="y")

    bottom_bar = ttk.Frame(self.zit_tab)
    bottom_bar.pack(fill="x", padx=8, pady=(0, 8))
    ttk.Button(bottom_bar, text="Editar seleccionado...", command=self.edit_selected_zit).pack(
        side="left"
    )

    self._setup_zit_comparator_ui(self.zit_comp_tab)

  def _setup_zit_comparator_ui(self, parent):
    file_frame = ttk.LabelFrame(parent, text=" Archivos a Comparar ")
    file_frame.pack(fill="x", padx=8, pady=8)

    row_a = ttk.Frame(file_frame)
    row_a.pack(fill="x", padx=6, pady=4)
    ttk.Label(row_a, text="Archivo ANTES (Original):", width=22).pack(side="left")
    self.zit_comp_path_a = tk.StringVar()
    ttk.Entry(row_a, textvariable=self.zit_comp_path_a).pack(side="left", fill="x", expand=True, padx=4)
    ttk.Button(row_a, text="Examinar...", command=lambda: self._browse_zit_comp_file(self.zit_comp_path_a)).pack(side="right")

    row_b = ttk.Frame(file_frame)
    row_b.pack(fill="x", padx=6, pady=(4, 8))
    ttk.Label(row_b, text="Archivo DESPUÉS (Nuevo):", width=22).pack(side="left")
    self.zit_comp_path_b = tk.StringVar()
    ttk.Entry(row_b, textvariable=self.zit_comp_path_b).pack(side="left", fill="x", expand=True, padx=4)
    ttk.Button(row_b, text="Examinar...", command=lambda: self._browse_zit_comp_file(self.zit_comp_path_b)).pack(side="right")

    btn_row = ttk.Frame(file_frame)
    btn_row.pack(fill="x", padx=6, pady=(0, 6))
    ttk.Button(btn_row, text="Ejecutar Comparación", command=self.run_zit_comparison).pack(side="left")
    ttk.Button(btn_row, text="Usar archivo abierto actual como 'DESPUÉS'", command=self.set_current_as_zit_comp_b).pack(side="left", padx=8)

    comp_cols = ("linea", "tipo", "detalle", "antes", "despues")
    comp_headers = {
        "linea": "Línea", "tipo": "Elemento", "detalle": "Cambio / Campo",
        "antes": "Valor ANTES", "despues": "Valor DESPUÉS"
    }
    comp_widths = {"linea": 60, "tipo": 90, "detalle": 180, "antes": 240, "despues": 240}

    comp_table_frame = ttk.Frame(parent)
    comp_table_frame.pack(fill="both", expand=True, padx=8, pady=(0, 8))

    self.zit_comp_tree = ttk.Treeview(comp_table_frame, columns=comp_cols, show="headings")
    for c in comp_cols:
      self.zit_comp_tree.heading(c, text=comp_headers[c])
      self.zit_comp_tree.column(c, width=comp_widths[c], anchor="w")
    self.zit_comp_tree.pack(side="left", fill="both", expand=True)

    comp_sb = ttk.Scrollbar(comp_table_frame, orient="vertical", command=self.zit_comp_tree.yview)
    self.zit_comp_tree.configure(yscroll=comp_sb.set)
    comp_sb.pack(side="right", fill="y")

  def _browse_zit_comp_file(self, string_var):
    path = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=[("Archivos de Modo Historia", "*.json *.gscf *.GSCF *.gsc *.txt"), ("Todos los archivos", "*.*")]
    )
    if path:
      string_var.set(path)

  def set_current_as_zit_comp_b(self):
    if self.file_path:
      self.zit_comp_path_b.set(self.file_path)
      messagebox.showinfo("Copiado", f"Se asignó el archivo actual como 'DESPUÉS':\n{os.path.basename(self.file_path)}")
    else:
      messagebox.showwarning("Aviso", "No hay ningún archivo abierto actualmente en el editor.")

  def run_zit_comparison(self):
    path_a = self.zit_comp_path_a.get().strip()
    path_b = self.zit_comp_path_b.get().strip()

    if not path_a or not path_b:
      messagebox.showwarning("Faltan rutas", "Por favor selecciona ambos archivos para comparar.")
      return

    if not os.path.exists(path_a) or not os.path.exists(path_b):
      messagebox.showerror("Error", "Uno de los archivos especificados no existe.")
      return

    try:
      with open(path_a, "r", encoding="utf-8", errors="replace") as f:
        lines_a = f.readlines()
      with open(path_b, "r", encoding="utf-8", errors="replace") as f:
        lines_b = f.readlines()
    except Exception as e:
      messagebox.showerror("Error de lectura", str(e))
      return

    self.zit_comp_tree.delete(*self.zit_comp_tree.get_children())

    n = min(len(lines_a), len(lines_b))
    total_line_diffs = 0
    total_zit_diffs = 0

    for i in range(n):
      la, lb = lines_a[i], lines_b[i]
      if la == lb:
        continue
      total_line_diffs += 1

      self.zit_comp_tree.insert("", "end", values=(i + 1, "Línea distinta", "Cambio en contenido de línea", la.strip(), lb.strip()))

      zits_a = {f"zit{m.group(1)}": m.group(2).upper() for m in ZIT_PATTERN.finditer(la)}
      zits_b = {f"zit{m.group(1)}": m.group(2).upper() for m in ZIT_PATTERN.finditer(lb)}

      all_fields = set(zits_a) | set(zits_b)
      for field in sorted(all_fields, key=lambda x: int(x[3:])):
        va = zits_a.get(field, "(no existe)")
        vb = zits_b.get(field, "(no existe)")
        if va != vb:
          total_zit_diffs += 1

          try:
            dec_a = int(va, 16) if va != "(no existe)" else None
            name_a = f" ({lookup_zitem(dec_a)})" if dec_a is not None else ""
          except ValueError:
            name_a = ""

          try:
            dec_b = int(vb, 16) if vb != "(no existe)" else None
            name_b = f" ({lookup_zitem(dec_b)})" if dec_b is not None else ""
          except ValueError:
            name_b = ""

          val_a_str = f"&{va}{name_a}" if va != "(no existe)" else va
          val_b_str = f"&{vb}{name_b}" if vb != "(no existe)" else vb

          self.zit_comp_tree.insert("", "end", values=("", f"Z-Item ({field})", f"Modificación de {field}", val_a_str, val_b_str))

    summary_msg = f"Comparación finalizada. Líneas distintas: {total_line_diffs} | Campos $zit distintos: {total_zit_diffs}"
    if total_line_diffs == 0:
      messagebox.showinfo("Resultado", "¡Los archivos son idénticos línea por línea!")
    else:
      messagebox.showinfo("Resultado", summary_msg)

  def refresh_zit_table(self):
    self.zit_manager.set_text(self.file_content)
    self.render_zit_rows(self.zit_manager.entries)

  def normalize_zits(self):
    if not self.file_content:
      messagebox.showinfo("Nada que normalizar", "Primero carga un archivo de Modo Historia.")
      return
    self.zit_manager.set_text(self.file_content)
    self.zit_manager.normalize_all_lines()
    self.file_content = self.zit_manager.get_text()
    self.render_zit_rows(self.zit_manager.entries)
    messagebox.showinfo(
        "Z-Items normalizados",
        "Los campos $zit del archivo cargado fueron ordenados y completados "
        "($zit8, $zit1..$zit7). Usa 'Guardar' para escribir los cambios en disco."
    )

  def render_zit_rows(self, entries):
    self.zit_tree.delete(*self.zit_tree.get_children())
    self.zit_row_to_entry.clear()
    for entry in entries:
      row_id = self.zit_tree.insert(
          "", "end",
          values=(
              entry["evento"], entry["actor"], entry["campo"],
              f"&{entry['hex']}", entry["dec"], entry["nombre"],
          ),
      )
      self.zit_row_to_entry[row_id] = entry

  def apply_zit_filter(self):
    term = self.zit_filter_var.get().strip().lower()
    if not term:
      self.render_zit_rows(self.zit_manager.entries)
      return
    filtered = [
        e for e in self.zit_manager.entries
        if term in str(e["evento"]).lower()
        or term in str(e["actor"]).lower()
        or term in str(e["campo"]).lower()
        or term in str(e["hex"]).lower()
        or term in str(e["dec"]).lower()
        or term in str(e["nombre"]).lower()
    ]
    self.render_zit_rows(filtered)

  def sort_zit_by(self, col):
    data = [(self.zit_tree.set(k, col), k) for k in self.zit_tree.get_children("")]
    try:
      data.sort(key=lambda t: int(t[0]))
    except ValueError:
      data.sort(key=lambda t: t[0].lower())
    for index, (_, k) in enumerate(data):
      self.zit_tree.move(k, "", index)

  def edit_selected_zit(self):
    if not self.file_content:
      messagebox.showinfo("Nada que editar", "Primero carga un archivo de Modo Historia.")
      return
    sel = self.zit_tree.selection()
    if not sel:
      messagebox.showinfo("Selecciona una fila", "Elige un campo $zit de la tabla primero.")
      return
    row_id = sel[0]
    entry = self.zit_row_to_entry.get(row_id)
    if entry is None:
      return

    def on_accept(new_dec):
      self.zit_manager.apply_edit(entry, new_dec)
      self.file_content = self.zit_manager.get_text()
      self.zit_tree.item(
          row_id,
          values=(
              entry["evento"], entry["actor"], entry["campo"],
              f"&{entry['hex']}", entry["dec"], entry["nombre"],
          ),
      )
      messagebox.showinfo(
          "Actualizado",
          f"{entry['campo']} de {entry['actor']} ({entry['evento']}) "
          f"actualizado a &{entry['hex']} -> {entry['nombre']}\n"
          "Usa 'Guardar' para escribir los cambios en disco."
      )

    ZitEditDialog(self.root, entry, on_accept)

  # ======================================================================
  # EDITOR DE POSICIÓN / ROTACIÓN ($Set_transform)
  # (integrado desde BT3_position_editor.py)
  # ======================================================================

  POS_SCALE = 2.2
  POS_COS_A = math.cos(math.radians(30)) * POS_SCALE
  POS_SIN_A = math.sin(math.radians(30)) * POS_SCALE
  POS_GRID_RANGE = 100
  POS_GRID_STEP = 20

  def setup_position_editor_ui(self, parent):
    top = ttk.Frame(parent, padding=6)
    top.pack(side="top", fill="x")
    ttk.Button(
        top, text="🔄 Recargar desde el archivo actual",
        command=self.parse_position_transforms,
    ).pack(side="left")
    ttk.Button(
        top, text="💾 Aplicar cambios de posición al archivo",
        command=self.save_position_changes,
    ).pack(side="left", padx=6)
    ttk.Label(
        top,
        text="(esto actualiza el contenido en memoria; usa Archivo > Guardar "
             "para escribirlo en disco)",
        foreground="#888888",
    ).pack(side="left", padx=6)

    body = ttk.Frame(parent)
    body.pack(side="top", fill="both", expand=True)

    # ---- panel izquierdo: lista de transforms ----
    left = ttk.Frame(body, padding=6)
    left.pack(side="left", fill="y")

    ttk.Label(left, text="Eventos / Actores ($Set_transform)", font=("", 10, "bold")).pack(anchor="w")

    list_frame = ttk.Frame(left)
    list_frame.pack(side="top", fill="y")
    self.pos_listbox = tk.Listbox(list_frame, width=28, height=28, exportselection=False)
    self.pos_listbox.pack(side="left", fill="y")
    pos_scroll = ttk.Scrollbar(list_frame, orient="vertical", command=self.pos_listbox.yview)
    pos_scroll.pack(side="left", fill="y")
    self.pos_listbox.config(yscrollcommand=pos_scroll.set)
    self.pos_listbox.bind("<<ListboxSelect>>", self.on_position_select)
    self.pos_listbox.bind("<Control-c>", lambda e: self.copy_position_current())
    self.pos_listbox.bind("<Control-v>", lambda e: self.paste_position_current())

    cp_row = ttk.Frame(left)
    cp_row.pack(fill="x", pady=(6, 0))
    ttk.Button(cp_row, text="Copiar (Ctrl+C)", command=self.copy_position_current).pack(side="left", fill="x", expand=True)
    ttk.Button(cp_row, text="Pegar (Ctrl+V)", command=self.paste_position_current).pack(side="left", fill="x", expand=True, padx=(4, 0))

    self.pos_clipboard_label = ttk.Label(left, text="Portapapeles: (vacío)", wraplength=210, foreground="#888888")
    self.pos_clipboard_label.pack(anchor="w", pady=(4, 0))

    # ---- panel central: canvas isométrico ----
    center = ttk.Frame(body, padding=6)
    center.pack(side="left", fill="both", expand=True)

    ttk.Label(
        center,
        text="Vista de referencia (suelo = X/Z, altura = Y). "
             "Clic o arrastra sobre el suelo para mover al actor seleccionado.",
        wraplength=520,
    ).pack(anchor="w")

    self.pos_canvas = tk.Canvas(center, width=620, height=520, bg="#101418", highlightthickness=0)
    self.pos_canvas.pack(pady=6)
    self.pos_canvas.bind("<Button-1>", self.on_position_canvas_click)
    self.pos_canvas.bind("<B1-Motion>", self.on_position_canvas_click)
    self.pos_canvas.bind("<Control-c>", lambda e: self.copy_position_current())
    self.pos_canvas.bind("<Control-v>", lambda e: self.paste_position_current())

    self.pos_legend = ttk.Label(center, text="")
    self.pos_legend.pack(anchor="w")

    # ---- panel derecho: controles numéricos ----
    right = ttk.Frame(body, padding=6)
    right.pack(side="left", fill="y")

    ttk.Label(right, text="Editar transform seleccionado", font=("", 10, "bold")).pack(anchor="w", pady=(0, 6))

    self.pos_actor_label = ttk.Label(right, text="Actor: -", font=("", 10, "bold"))
    self.pos_actor_label.pack(anchor="w")
    self.pos_event_label = ttk.Label(right, text="Evento: -")
    self.pos_event_label.pack(anchor="w", pady=(0, 10))

    self.pos_sliders = {}
    self.pos_entries = {}
    specs = [
        ("loc", 0, "Posición X", -150, 150),
        ("loc", 1, "Posición Y (altura)", -50, 50),
        ("loc", 2, "Posición Z (profundidad)", -150, 150),
        ("rot", 0, "Rotación X (pitch)", -180, 180),
        ("rot", 1, "Rotación Y (yaw)", -180, 180),
        ("rot", 2, "Rotación Z (roll)", -180, 180),
    ]
    for group, idx, label, lo, hi in specs:
      frame = ttk.Frame(right)
      frame.pack(fill="x", pady=4)
      ttk.Label(frame, text=label, width=22).pack(anchor="w")

      row = ttk.Frame(frame)
      row.pack(fill="x")

      var = tk.DoubleVar(value=0.0)
      scale = ttk.Scale(
          row, from_=lo, to=hi, orient="horizontal", variable=var,
          command=lambda v, g=group, i=idx: self.on_position_slider_change(g, i),
      )
      scale.pack(side="left", fill="x", expand=True)

      entry = ttk.Entry(row, width=9)
      entry.pack(side="left", padx=4)
      entry.bind("<Return>", lambda e, g=group, i=idx: self.on_position_entry_change(g, i))

      self.pos_sliders[(group, idx)] = var
      self.pos_entries[(group, idx)] = entry

    ttk.Button(right, text="Aplicar a este transform", command=self.apply_position_current).pack(fill="x", pady=(14, 4))
    ttk.Label(
        right,
        text="(los cambios se aplican en memoria;\nusa 'Aplicar cambios de posición\nal archivo' para escribirlos\nal contenido del archivo)",
        foreground="#888888",
    ).pack(anchor="w")

    self.pos_status = ttk.Label(parent, text="Carga un archivo para ver los $Set_transform.", anchor="w", relief="sunken")
    self.pos_status.pack(side="bottom", fill="x")

  # -------------------------------------------------------- parseo/carga --
  def parse_position_transforms(self):
    if not self.file_content:
      self.pos_transforms = []
      self.pos_selected = None
      if hasattr(self, "pos_listbox"):
        self.pos_listbox.delete(0, "end")
        self.draw_position_scene()
        self.pos_status.config(text="Carga un archivo para ver los $Set_transform.")
      return

    self.pos_transforms = parse_pos_transforms(self.file_content)
    self.pos_selected = None
    self.refresh_position_listbox()

    self.pos_status.config(
        text=f"{len(self.pos_transforms)} bloques $Set_transform encontrados."
    )
    if self.pos_transforms:
      self.pos_listbox.selection_set(0)
      self.on_position_select()
    else:
      self.draw_position_scene()

  def refresh_position_listbox(self):
    self.pos_listbox.delete(0, "end")
    for t in self.pos_transforms:
      label = t.label() + ("  *" if t.modified else "")
      self.pos_listbox.insert("end", label)

  # --------------------------------------------------------- selección --
  def on_position_select(self, event=None):
    sel = self.pos_listbox.curselection()
    if not sel:
      return
    self.pos_selected = self.pos_transforms[sel[0]]
    self.sync_position_fields()
    self.draw_position_scene()

  def sync_position_fields(self):
    t = self.pos_selected
    if not t:
      return
    self.pos_updating_fields = True
    self.pos_actor_label.config(text=f"Actor: {t.actor}")
    self.pos_event_label.config(text=f"Evento: {t.event}")
    for i in range(3):
      self.pos_sliders[("loc", i)].set(t.loc[i])
      self.pos_entries[("loc", i)].delete(0, "end")
      self.pos_entries[("loc", i)].insert(0, f"{t.loc[i]:.2f}")
      self.pos_sliders[("rot", i)].set(t.rot[i])
      self.pos_entries[("rot", i)].delete(0, "end")
      self.pos_entries[("rot", i)].insert(0, f"{t.rot[i]:.2f}")
    self.pos_updating_fields = False

  # ------------------------------------------------------------ edición --
  def on_position_slider_change(self, group, idx):
    if self.pos_updating_fields or not self.pos_selected:
      return
    value = self.pos_sliders[(group, idx)].get()
    getattr(self.pos_selected, group)[idx] = value
    self.pos_selected.modified = True
    entry = self.pos_entries[(group, idx)]
    entry.delete(0, "end")
    entry.insert(0, f"{value:.2f}")
    self.draw_position_scene()

  def on_position_entry_change(self, group, idx):
    if not self.pos_selected:
      return
    try:
      value = float(self.pos_entries[(group, idx)].get())
    except ValueError:
      return
    getattr(self.pos_selected, group)[idx] = value
    self.pos_selected.modified = True
    self.pos_sliders[(group, idx)].set(value)
    self.draw_position_scene()

  def apply_position_current(self):
    if not self.pos_selected:
      return
    self.pos_selected.modified = True
    idx = self.pos_transforms.index(self.pos_selected)
    self.refresh_position_listbox()
    self.pos_listbox.selection_set(idx)
    self.pos_status.config(
        text=f"Cambios aplicados en memoria a {self.pos_selected.actor} ({self.pos_selected.event})."
    )
    self.draw_position_scene()

  # ----------------------------------------------------- copiar/pegar --
  def copy_position_current(self):
    if not self.pos_selected:
      return
    self.pos_clipboard = (list(self.pos_selected.loc), list(self.pos_selected.rot))

    try:
      self.root.clipboard_clear()
      self.root.clipboard_append(self.pos_selected.format())
    except tk.TclError:
      pass

    self.pos_clipboard_label.config(
        text=f"Portapapeles: {self.pos_selected.actor} ({self.pos_selected.event})\n"
             f"loc={tuple(round(v, 2) for v in self.pos_selected.loc)}\n"
             f"rot={tuple(round(v, 2) for v in self.pos_selected.rot)}"
    )
    self.pos_status.config(text=f"Copiado: {self.pos_selected.actor} ({self.pos_selected.event}).")

  def paste_position_current(self):
    if not self.pos_selected:
      return

    loc, rot = None, None

    if self.pos_clipboard is not None:
      loc, rot = self.pos_clipboard
    else:
      try:
        text = self.root.clipboard_get()
      except tk.TclError:
        text = ""
      m = POS_TRANSFORM_RE.search(text)
      if m:
        loc = (float(m.group("lx")), float(m.group("ly")), float(m.group("lz")))
        rot = (float(m.group("rx")), float(m.group("ry")), float(m.group("rz")))

    if loc is None:
      messagebox.showinfo(
          "Nada para pegar",
          "Primero copia un $Set_transform (Ctrl+C), o pega un texto\n"
          "de la forma $Set_transform:{$actor:$X $loc:F[...] $rot:F[...]}\n"
          "en el portapapeles del sistema.",
      )
      return

    self.pos_selected.loc = list(loc)
    self.pos_selected.rot = list(rot)
    self.pos_selected.modified = True
    self.sync_position_fields()

    idx = self.pos_transforms.index(self.pos_selected)
    self.refresh_position_listbox()
    self.pos_listbox.selection_set(idx)

    self.draw_position_scene()
    self.pos_status.config(text=f"Pegado en: {self.pos_selected.actor} ({self.pos_selected.event}).")

  # ------------------------------------------------------- canvas iso --
  def pos_world_to_screen(self, x, y, z):
    cx, cy = 310, 280
    sx = cx + (x - z) * self.POS_COS_A
    sy = cy + (x + z) * self.POS_SIN_A - y * self.POS_SCALE
    return sx, sy

  def pos_screen_to_world_floor(self, sx, sy):
    cx, cy = 310, 280
    dx = sx - cx
    dy = sy - cy
    a = dx / self.POS_COS_A
    b = dy / self.POS_SIN_A
    x = (a + b) / 2
    z = (b - a) / 2
    return x, z

  def draw_position_scene(self):
    if not hasattr(self, "pos_canvas"):
      return
    c = self.pos_canvas
    c.delete("all")

    rng = self.POS_GRID_RANGE
    step = self.POS_GRID_STEP
    for v in range(-rng, rng + 1, step):
      p1 = self.pos_world_to_screen(v, 0, -rng)
      p2 = self.pos_world_to_screen(v, 0, rng)
      c.create_line(*p1, *p2, fill="#233042")
      p3 = self.pos_world_to_screen(-rng, 0, v)
      p4 = self.pos_world_to_screen(rng, 0, v)
      c.create_line(*p3, *p4, fill="#233042")

    ox = self.pos_world_to_screen(-rng, 0, 0)
    oxe = self.pos_world_to_screen(rng, 0, 0)
    c.create_line(*ox, *oxe, fill="#3d5a80", width=2)
    c.create_text(*self.pos_world_to_screen(rng + 8, 0, 0), text="X", fill="#3d5a80")

    oz = self.pos_world_to_screen(0, 0, -rng)
    oze = self.pos_world_to_screen(0, 0, rng)
    c.create_line(*oz, *oze, fill="#5a3d80", width=2)
    c.create_text(*self.pos_world_to_screen(0, 0, rng + 8), text="Z (profundidad)", fill="#5a3d80")

    oy = self.pos_world_to_screen(0, 0, 0)
    oye = self.pos_world_to_screen(0, 40, 0)
    c.create_line(*oy, *oye, fill="#808080", dash=(3, 2))
    c.create_text(*self.pos_world_to_screen(0, 44, 0), text="Y (altura)", fill="#808080")

    if not self.pos_selected:
      return

    same_event = [t for t in self.pos_transforms if t.event == self.pos_selected.event]
    for t in same_event:
      x, y, z = t.loc
      sx, sy = self.pos_world_to_screen(x, y, z)
      is_sel = (t is self.pos_selected)
      r = 10 if is_sel else 7
      color = pos_color_for(t.actor)
      outline = "#FFFFFF" if is_sel else color

      floor_sx, floor_sy = self.pos_world_to_screen(x, 0, z)
      if abs(y) > 0.01:
        c.create_line(sx, sy, floor_sx, floor_sy, fill="#555", dash=(2, 2))

      c.create_oval(sx - r, sy - r, sx + r, sy + r, fill=color, outline=outline, width=2)
      c.create_text(sx, sy - r - 10, text=t.actor, fill="white", font=("", 9, "bold" if is_sel else "normal"))

      yaw = math.radians(t.rot[1])
      arrow_len = 16
      ax = x + arrow_len * math.sin(yaw)
      az = z + arrow_len * math.cos(yaw)
      asx, asy = self.pos_world_to_screen(ax, y, az)
      c.create_line(sx, sy, asx, asy, fill=outline, width=2, arrow="last")

    self.pos_legend.config(
        text=f"Editando: {self.pos_selected.actor}  en  {self.pos_selected.event}   "
             f"|  loc=({self.pos_selected.loc[0]:.2f}, {self.pos_selected.loc[1]:.2f}, {self.pos_selected.loc[2]:.2f})  "
             f"rot=({self.pos_selected.rot[0]:.2f}, {self.pos_selected.rot[1]:.2f}, {self.pos_selected.rot[2]:.2f})"
    )

  def on_position_canvas_click(self, event):
    if not self.pos_selected:
      return
    x, z = self.pos_screen_to_world_floor(event.x, event.y)
    self.pos_selected.loc[0] = x
    self.pos_selected.loc[2] = z
    self.pos_selected.modified = True
    self.sync_position_fields()
    self.draw_position_scene()

  # ------------------------------------------------------------- guardar --
  def save_position_changes(self):
    if not self.file_content:
      messagebox.showwarning("Atención", "Carga un archivo primero.")
      return

    modified = [t for t in self.pos_transforms if t.modified]
    if not modified:
      messagebox.showinfo("Nada que guardar", "No hay cambios de posición pendientes.")
      return

    text = self.file_content
    for t in sorted(modified, key=lambda t: t.start, reverse=True):
      text = text[:t.start] + t.format() + text[t.end:]

    self.file_content = text
    self.parse_position_transforms()

    self.pos_status.config(
        text=f"{len(modified)} transform(s) aplicados al contenido del archivo (en memoria)."
    )
    messagebox.showinfo(
        "Aplicado",
        f"{len(modified)} bloque(s) $Set_transform actualizados en el archivo.\n"
        "Usa Archivo > Guardar (o Guardar como...) para escribirlo en disco.",
    )

  def load_file(self):
    path = filedialog.askopenfilename(
        filetypes=[
            ("Archivos GSCF / JSON", "*.json *.GSCF *.gsc"),
            ("Todos los Archivos", "*.*"),
        ]
    )
    if not path:
      return

    try:
      with open(path, "r", encoding="utf-8-sig", errors="ignore") as f:
        self.file_content = f.read()

      self.file_path = path
      self.lbl_file.config(text=f"Archivo cargado: {os.path.basename(path)}")

      self.parse_json_data()
      self.parse_events_file()
      self.parse_animations_file()
      self.refresh_tables()
      self.refresh_zit_table()
      self.parse_position_transforms()

    except Exception as e:
      messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

  def parse_json_data(self):
    match_map = re.search(r"\$map:\s*(\d+)", self.file_content)
    if match_map:
      self.cmb_map.set(MAPS.get(match_map.group(1), MAPS["0"]))

    match_bgm = re.search(r"\$bgm:\s*(\d+)", self.file_content)
    if match_bgm:
      self.cmb_bgm.set(BGMS.get(match_bgm.group(1), BGMS["0"]))

    for i in range(5):
      self.read_actor_info(
          f"pla{i}",
          self.cmb_players[i],
          self.cmb_player_costumes[i],
          self.chk_player_dmg[i],
          self.ent_player_hp[i],
          self.ent_player_ia[i],
          i,
      )
      self.read_actor_info(
          f"cpu{i}",
          self.cmb_cpus[i],
          self.cmb_cpu_costumes[i],
          self.chk_cpu_dmg[i],
          self.ent_cpu_hp[i],
          self.ent_cpu_ia[i],
          i,
          default_ia="9",
      )

  def read_actor_info(
      self,
      actor_tag,
      cmb_char,
      cmb_cost,
      var_dmg,
      ent_hp,
      ent_ia,
      index,
      default_ia="0",
  ):
    pattern = (
        rf"\$Actor:\s*\{{[^}}]*?\$name:\s*[\"\']?\${actor_tag}\b[\"\']?[^}}]*?\}}"
    )
    match = re.search(pattern, self.file_content, re.IGNORECASE)

    if match:
      line_text = match.group(0)

      match_chr = re.search(r"\$chr:\s*&([0-9A-Fa-f]+)", line_text)
      if match_chr:
        char_dec = str(int(match_chr.group(1), 16))
        cmb_char.set(CHARACTERS_STORY.get(char_dec, CHARACTERS_STORY["0"]))

      match_cost = re.search(r"\$ctm:\s*(\d+)", line_text)
      if match_cost:
        cmb_cost.set(COSTUMES.get(match_cost.group(1), COSTUMES["0"]))

      match_dmg = re.search(r"\$dmg:\s*(\d+)", line_text)
      if match_dmg:
        var_dmg.set(int(match_dmg.group(1)))
      else:
        var_dmg.set(0)

      match_hp = re.search(r"\$hp:\s*(\d+)", line_text)
      ent_hp.delete(0, tk.END)
      ent_hp.insert(0, match_hp.group(1) if match_hp else "30000")

      match_ia = re.search(r"\$ia:\s*(\d+)", line_text)
      ent_ia.delete(0, tk.END)
      ent_ia.insert(0, match_ia.group(1) if match_ia else default_ia)
    else:
      if index > 0:
        cmb_char.set(EMPTY_SLOT)
      var_dmg.set(0)
      ent_hp.delete(0, tk.END)
      ent_hp.insert(0, "30000")
      ent_ia.delete(0, tk.END)
      ent_ia.insert(0, default_ia)

  def parse_events_file(self):
    self.triggers_list = []
    self.events_list = []

    ev_matches = list(
        re.finditer(r'["\']?(\$EV_\w+|EV_\w+)["\']?', self.file_content)
    )

    trig_pattern = re.compile(
        r'\{\s*\$if\s*:\s*&([0-9a-fA-F]+)[\s,]+\$to\s*:\s*(\$EV_\w+|\w+)\s*\}',
        re.IGNORECASE,
    )

    for match in trig_pattern.finditer(self.file_content):
      if_pos = match.start()
      parent_ev = "DESCONOCIDO"
      for ev_m in reversed(ev_matches):
        if ev_m.start() < if_pos:
          parent_ev = ev_m.group(1).replace('"', "").replace("'", "")
          break

      self.triggers_list.append({
          "ev_id": parent_ev,
          "block_raw": match.group(0),
          "if_raw": match.group(1),
          "to_raw": match.group(2),
      })

    full_event_pattern = re.compile(
        r'(\$Set_plafield:[^\n\r]*[\r\n]+\s*\$Set_cpufield:[^\n\r]*[\r\n]+\s*\$Event:\s*\{[^\}]*?\$evt:\s*&?([0-9a-fA-F]{4})\s+\$flag:\s*&?([0-9a-fA-F]{8})[^\}]*\})',
        re.IGNORECASE,
    )

    for match in full_event_pattern.finditer(self.file_content):
      full_block = match.group(1)
      evt_hex = match.group(2)
      flag_hex = match.group(3)
      cmd_pos = match.start()

      parent_ev = "DESCONOCIDO"
      for ev_m in reversed(ev_matches):
        if ev_m.start() < cmd_pos:
          parent_ev = ev_m.group(1).replace('"', "").replace("'", "")
          break

      self.events_list.append({
          "ev_id": parent_ev,
          "block_raw": full_block,
          "evt_hex": evt_hex,
          "flag_hex": flag_hex,
      })

  def parse_animations_file(self):
    self.anims_list = []
    ev_matches = list(
        re.finditer(r'["\']?(\$EV_\w+|EV_\w+)["\']?', self.file_content)
    )

    anim_pattern = re.compile(
        r'(\$Load_Anim\s*:\s*\{[^}]*?\$actor\s*:\s*(\$[\w\d]+)[^}]*?\$anm\s*:\s*&([0-9a-fA-F]+)[^}]*\})(?:\s*[\r\n]*\s*(\$Loop|\$Wait))?',
        re.IGNORECASE,
    )

    for match in anim_pattern.finditer(self.file_content):
      full_block = match.group(0)
      anim_block_only = match.group(1)
      actor_name = match.group(2)
      anm_hex = match.group(3).upper()
      mode = match.group(4) if match.group(4) else ""
      pos = match.start()

      parent_ev = "DESCONOCIDO"
      for ev_m in reversed(ev_matches):
        if ev_m.start() < pos:
          parent_ev = ev_m.group(1).replace('"', "").replace("'", "")
          break

      self.anims_list.append({
          "ev_id": parent_ev,
          "full_block_raw": full_block,
          "anim_block_only": anim_block_only,
          "actor": actor_name,
          "anm_hex": anm_hex,
          "mode": mode,
      })

  def refresh_tables(self):
    for item in self.tree_triggers.get_children():
      self.tree_triggers.delete(item)
    for item in self.tree_events.get_children():
      self.tree_events.delete(item)
    for item in self.tree_anims.get_children():
      self.tree_anims.delete(item)

    for idx, item in enumerate(self.triggers_list):
      norm_hex = normalize_hex(item["if_raw"], HEX_TO_LABEL_COND)
      desc = HEX_TO_LABEL_COND.get(norm_hex, "DESCONOCIDO / Custom Condition")
      self.tree_triggers.insert(
          "",
          "end",
          iid=str(idx),
          values=(item["ev_id"], item["if_raw"], desc, item["to_raw"]),
      )

    for idx, item in enumerate(self.events_list):
      norm_hex = normalize_hex(item["evt_hex"], HEX_TO_LABEL_EVENT)
      desc = HEX_TO_LABEL_EVENT.get(norm_hex, "DESCONOCIDO / Custom Event")

      if is_char_event(desc):
        char_hex_code = item["flag_hex"][-2:].upper()
        char_name = CHARACTERS_EVENTS.get(char_hex_code, "Desconocido")
        char_display = f"{char_hex_code} - {char_name}"
      else:
        char_display = "N/A"

      self.tree_events.insert(
          "",
          "end",
          iid=str(idx),
          values=(
              item["ev_id"],
              item["evt_hex"],
              desc,
              item["flag_hex"],
              char_display,
          ),
      )

    for idx, item in enumerate(self.anims_list):
      clean_hex = item["anm_hex"].lstrip("0") or "000"
      if len(clean_hex) == 1:
        clean_hex = "00" + clean_hex
      elif len(clean_hex) == 2:
        clean_hex = "0" + clean_hex

      anim_name = ANIMATIONS.get(
          clean_hex,
          ANIMATIONS.get(
              item["anm_hex"], "Animación Personalizada / Desconocida"
          ),
      )
      self.tree_anims.insert(
          "",
          "end",
          iid=str(idx),
          values=(
              item["ev_id"],
              item["actor"],
              item["anm_hex"],
              anim_name,
              item.get("mode", ""),
          ),
      )

  def on_trig_select(self, event):
    sel = self.tree_triggers.selection()
    if not sel:
      return
    self.selected_trig_idx = int(sel[0])
    item = self.triggers_list[self.selected_trig_idx]

    self.ent_trig_id.config(state="normal")
    self.ent_trig_id.delete(0, tk.END)
    self.ent_trig_id.insert(0, item["ev_id"])
    self.ent_trig_id.config(state="readonly")

    norm_hex = normalize_hex(item["if_raw"], HEX_TO_LABEL_COND)
    desc = HEX_TO_LABEL_COND.get(norm_hex, None)
    if desc in HEX_CONDITIONS:
      self.cmb_trig_cond.set(desc)
    else:
      self.cmb_trig_cond.set(item["if_raw"])

    self.ent_trig_target.delete(0, tk.END)
    self.ent_trig_target.insert(0, item["to_raw"])

  def on_ev_select(self, event):
    sel = self.tree_events.selection()
    if not sel:
      return
    self.selected_ev_idx = int(sel[0])
    item = self.events_list[self.selected_ev_idx]

    self.ent_ev_id.config(state="normal")
    self.ent_ev_id.delete(0, tk.END)
    self.ent_ev_id.insert(0, item["ev_id"])
    self.ent_ev_id.config(state="readonly")

    norm_hex = normalize_hex(item["evt_hex"], HEX_TO_LABEL_EVENT)
    desc = HEX_TO_LABEL_EVENT.get(norm_hex, None)
    if desc in HEX_EVENTS:
      self.cmb_ev_select.set(desc)
    else:
      self.cmb_ev_select.set(item["evt_hex"])

    if is_char_event(desc or ""):
      self.cmb_char_select.config(state="readonly")
      char_hex_code = item["flag_hex"][-2:].upper()
      if char_hex_code in CHARACTERS_EVENTS:
        self.cmb_char_select.set(
            f"{char_hex_code} - {CHARACTERS_EVENTS[char_hex_code]}"
        )
    else:
      self.cmb_char_select.config(state="disabled")

  def on_anim_select(self, event):
    sel = self.tree_anims.selection()
    if not sel:
      return
    self.selected_anim_idx = int(sel[0])
    item = self.anims_list[self.selected_anim_idx]

    self.ent_anim_id.config(state="normal")
    self.ent_anim_id.delete(0, tk.END)
    self.ent_anim_id.insert(0, item["ev_id"])
    self.ent_anim_id.config(state="readonly")

    self.ent_anim_actor.config(state="normal")
    self.ent_anim_actor.delete(0, tk.END)
    self.ent_anim_actor.insert(0, item["actor"])
    self.ent_anim_actor.config(state="readonly")

    mode_val = item.get("mode", "").strip()
    if mode_val.lower() == "$loop":
      self.cmb_anim_mode.set("$Loop")
    elif mode_val.lower() == "$wait":
      self.cmb_anim_mode.set("$Wait")
    else:
      self.cmb_anim_mode.set("")

    clean_hex = item["anm_hex"].lstrip("0") or "000"
    if len(clean_hex) == 1:
      clean_hex = "00" + clean_hex
    elif len(clean_hex) == 2:
      clean_hex = "0" + clean_hex

    for val in ANIMATION_LIST_LABELS:
      if val.startswith(clean_hex + " ") or val.startswith(
          item["anm_hex"] + " "
      ):
        self.cmb_anim_select.set(val)
        break

  def on_evt_combo_change(self, event=None):
    ev_label = self.cmb_ev_select.get()
    if is_char_event(ev_label):
      self.cmb_char_select.config(state="readonly")
    else:
      self.cmb_char_select.config(state="disabled")

  def replace_trigger(self):
    if self.selected_trig_idx is None:
      messagebox.showwarning(
          "Atención",
          "Selecciona una fila en la tabla de Desencadenadores primero.",
      )
      return

    cond_label = self.cmb_trig_cond.get()
    new_hex = HEX_CONDITIONS.get(cond_label, cond_label)
    new_to = self.ent_trig_target.get().strip()

    item = self.triggers_list[self.selected_trig_idx]
    old_block = item["block_raw"]
    new_block = f"{{$if:&{new_hex}, $to:{new_to}}}"

    if old_block in self.file_content:
      self.file_content = self.file_content.replace(old_block, new_block, 1)
      self.parse_events_file()
      self.parse_animations_file()
      self.refresh_tables()
      messagebox.showinfo(
          "Éxito", f"Desencadenador modificado correctamente:\n{new_block}"
      )
    else:
      messagebox.showerror(
          "Error", "No se encontró el desencadenador original en el archivo."
      )

  def replace_event(self):
        if self.selected_ev_idx is None:
            messagebox.showwarning(
                "Atención", "Selecciona una fila en la tabla de Eventos primero."
            )
            return

        ev_label = self.cmb_ev_select.get()
        new_evt_hex = HEX_EVENTS.get(ev_label, ev_label)

        if is_char_event(ev_label):
            char_label = self.cmb_char_select.get()
            char_hex_code = char_label.split(" - ")[0].strip()
            new_flag_hex = f"000000{char_hex_code}"
        else:
            new_flag_hex = "FFFFFFFF"

        item = self.events_list[self.selected_ev_idx]
        old_block = item["block_raw"]

        sangria = "         "  # 9 espacios de sangría exacta

        if "[CPU]" in ev_label:
            # Mapeo según el evento de CPU seleccionado (de 8011 a 8015)
            if new_evt_hex == "8011":
                cpufield = "<$actor:$cpu0 >"
            elif new_evt_hex == "8012":
                cpufield = "<$actor:$cpu1 >"
            elif new_evt_hex == "8013":
                cpufield = "<$actor:$cpu2 >"
            elif new_evt_hex == "8014":
                cpufield = "<$actor:$cpu3 >"
            elif new_evt_hex == "8015":
                cpufield = "<$actor:$cpu4 >"
            else:
                cpufield = "<$actor:$cpu0 >"

            plafield = "<$addHp:100 >"
        else:
            plafield = "<$actor:$pla1 >"
            cpufield = "null"

        new_block = (
            f"$Set_plafield:{plafield}\n"
            f"{sangria}$Set_cpufield:{cpufield}\n"
            f"{sangria}$Event:{{$evt: &{new_evt_hex} $flag: &{new_flag_hex}}}"
        )

        sangria = "         "  # 9 espacios de sangría exacta

        new_block = (
            f"$Set_plafield:{plafield}\n"
            f"{sangria}$Set_cpufield:{cpufield}\n"
            f"{sangria}$Event:{{$evt: &{new_evt_hex} $flag: &{new_flag_hex}}}"
        )

        if old_block in self.file_content:
            self.file_content = self.file_content.replace(old_block, new_block, 1)
            self.parse_events_file()
            self.parse_animations_file()
            self.refresh_tables()
            messagebox.showinfo(
                "Éxito",
                f"Evento y Personaje de {item['ev_id']} modificado correctamente.",
            )
        else:
            messagebox.showerror(
                "Error", "No se encontró el evento original en el archivo."
      )

  def replace_animation(self):
    if self.selected_anim_idx is None:
      messagebox.showwarning(
          "Atención", "Selecciona una fila en la pestaña de Animaciones primero."
      )
      return

    selected_anim_text = self.cmb_anim_select.get()
    if not selected_anim_text:
      return

    new_anm_hex = selected_anim_text.split(" - ")[0].strip()
    new_mode = self.cmb_anim_mode.get().strip()

    item = self.anims_list[self.selected_anim_idx]
    old_full_block = item["full_block_raw"]
    old_anim_block = item["anim_block_only"]

    new_anim_block = re.sub(
        r"(\$anm\s*:\s*&?)[0-9a-fA-F]+",
        rf"\g<1>{new_anm_hex}",
        old_anim_block,
        flags=re.IGNORECASE,
    )

    line_start_idx = self.file_content.rfind('\n', 0, self.file_content.find(old_anim_block))
    if line_start_idx == -1:
      line_start_idx = 0
    else:
      line_start_idx += 1
    
    current_line = self.file_content[line_start_idx:self.file_content.find(old_anim_block) + len(old_anim_block)]
    indent_match = re.match(r"^([ \t]*)", current_line)
    indent = indent_match.group(1) if indent_match else "        "

    if new_mode:
      new_full_block = f"{new_anim_block}\n{indent}{new_mode}"
    else:
      new_full_block = new_anim_block

    if old_full_block in self.file_content:
      self.file_content = self.file_content.replace(
          old_full_block, new_full_block, 1
      )
    elif old_anim_block in self.file_content:
      self.file_content = self.file_content.replace(
          old_anim_block, new_full_block, 1
      )
    else:
      messagebox.showerror(
          "Error", "No se encontró el bloque de animación original en el archivo."
      )
      return

    self.parse_events_file()
    self.parse_animations_file()
    self.refresh_tables()

    modo_msg = new_mode if new_mode else "Ninguno"
    messagebox.showinfo(
        "Éxito",
        f"Animación y ejecución actualizadas correctamente.\nModo: {modo_msg}",
    )

  def process_updated_content(self):
    if not self.file_content:
      messagebox.showwarning("Atención", "Carga un archivo primero.")
      return None

    content = self.file_content
    map_key = [k for k, v in MAPS.items() if v == self.cmb_map.get()][0]
    bgm_key = [k for k, v in BGMS.items() if v == self.cmb_bgm.get()][0]

    content = re.sub(r"(\$map:\s*)\d+", r"\g<1>" + str(map_key), content)
    content = re.sub(r"(\$bgm:\s*)\d+", r"\g<1>" + str(bgm_key), content)

    # 0. Conservar los campos $zit ya existentes de cada actor (por si fueron
    #    editados en la pestaña "Z-Items") antes de reconstruir los bloques $Actor.
    existing_actor_zits = {}
    for m in re.finditer(r"\$Actor:\s*\{([^}]*)\}", content):
      block = m.group(1)
      name_m = re.search(r"\$name:\s*\$?(\w+)", block)
      if not name_m:
        continue
      zit_fields = re.findall(r"\$zit\d+\s*:\s*&[0-9A-Fa-f]+", block)
      if zit_fields:
        existing_actor_zits[name_m.group(1)] = " ".join(zit_fields)

    # 1. Eliminar todos los bloques de actores existentes para evitar duplicados o desorden
    content = re.sub(r"\$Actor:\s*\{[^}]*?\}\s*", "", content)

    # 2. Generar la lista ordenada de nuevos actores con sangría fija de 9 espacios
    new_actors_lines = []
    sangria = "         "  # 9 espacios de indentación exacta

    # Recopilar jugadores activos
    active_players = 0
    for i in range(5):
      val = self.cmb_players[i].get()
      if val != EMPTY_SLOT:
        active_players = i + 1
        char_id = [k for k, v in CHARACTERS_STORY.items() if v == val][0]
        char_hex = f"{int(char_id):04X}"
        cost_val = self.cmb_player_costumes[i].get()
        cost_id = [k for k, v in COSTUMES.items() if v == cost_val][0]
        dmg_val = self.chk_player_dmg[i].get()
        hp_val = self.ent_player_hp[i].get().strip() or "30000"
        ia_val = self.ent_player_ia[i].get().strip() or "0"
        zit_block = existing_actor_zits.get(f"pla{i}", "$zit8: &00000089")

        actor_str = f"{sangria}$Actor:{{$name:$pla{i} $chr: &{char_hex} $ctm: {cost_id} $dmg: {dmg_val} $ia: {ia_val} {zit_block} $hp: {hp_val}}}"
        new_actors_lines.append(actor_str)

    # Recopilar rivales CPU activos
    active_cpus = 0
    for i in range(5):
      val = self.cmb_cpus[i].get()
      if val != EMPTY_SLOT:
        active_cpus = i + 1
        char_id = [k for k, v in CHARACTERS_STORY.items() if v == val][0]
        char_hex = f"{int(char_id):04X}"
        cost_val = self.cmb_cpu_costumes[i].get()
        cost_id = [k for k, v in COSTUMES.items() if v == cost_val][0]
        dmg_val = self.chk_cpu_dmg[i].get()
        hp_val = self.ent_cpu_hp[i].get().strip() or "30000"
        ia_val = self.ent_cpu_ia[i].get().strip() or "9"
        zit_block = existing_actor_zits.get(f"cpu{i}", "$zit8: &00000089")

        actor_str = f"{sangria}$Actor:{{$name:$cpu{i} $chr: &{char_hex} $ctm: {cost_id} $dmg: {dmg_val} $ia: {ia_val} {zit_block} $hp: {hp_val}}}"
        new_actors_lines.append(actor_str)

    # Actualizar los conteos en las líneas de $Role si existen
    content = re.sub(r"(\$Role:\s*\{\s*\$type:\s*0,\s*\$count:\s*)\d+", rf"\g<1>{active_players}", content)
    content = re.sub(r"(\$Role:\s*\{\s*\$type:\s*1,\s*\$count:\s*)\d+", rf"\g<1>{active_cpus}", content)

    # 3. Insertar los actores ordenados justo después de la última línea de $Role o de $Setting
    actors_block = "\n" + "\n".join(new_actors_lines) + "\n"
    
    role_matches = list(re.finditer(r"\$Role:\s*\{[^}]*\}", content))
    if role_matches:
      last_role_end = role_matches[-1].end()
      content = content[:last_role_end] + actors_block + content[last_role_end:]
    else:
      setting_match = re.search(r"\$Setting:\s*\{[^}]*\}", content)
      if setting_match:
        pos = setting_match.end()
        content = content[:pos] + actors_block + content[pos:]

    return content

  def save_file(self):
    content = self.process_updated_content()
    if content is None:
      return

    if self.file_path:
      try:
        with open(self.file_path, "w", encoding="utf-8", newline="") as f:
          f.write(content)
        self.file_content = content
        self.refresh_zit_table()
        messagebox.showinfo(
            "Éxito", "Los cambios han sido guardados correctamente."
        )
      except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
    else:
      self.save_file_as()

  def save_file_as(self):
    content = self.process_updated_content()
    if content is None:
      return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[
            ("Archivos JSON", "*.json"),
            ("Archivos GSCF", "*.GSCF"),
            ("Todos los Archivos", "*.GSCF *.gsc"),
        ],
    )

    if save_path:
      try:
        with open(save_path, "w", encoding="utf-8", newline="") as f:
          f.write(content)
        self.file_path = save_path
        self.file_content = content
        self.lbl_file.config(
            text=f"Archivo cargado: {os.path.basename(save_path)}"
        )
        self.refresh_zit_table()
        messagebox.showinfo(
            "Éxito", "El archivo se guardó en la ubicación elegida."
        )
      except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")


if __name__ == "__main__":
  try:
    root = tk.Tk()
    try:
        root.iconbitmap('BT3_no_green.ico')
    except tk.TclError:
        pass
    app = BT3CombinedEditor(root)
    root.mainloop()
  except Exception as e:
    import traceback

    print("Error crítico al iniciar la aplicación:")
    traceback.print_exc()
    input("Presiona Enter para salir...")