import pykakasi
import json
from braille_table import BRAILLE_TABLE

def convert_to_romaji(text):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "H")        # Japanese to Hiragana
    kakasi.setMode("C", False)      # no capitalize
    conv = kakasi.getConverter()
    result = conv.do(text)
    return result

def generate_template_json():
	template_json = {}
	template_json["title"] = input("曲のタイトル：")
	template_json["bpm"] = input("曲のbpm：")
	template_json["notes"] = []

	return template_json

def add_char_data(json_file, chars):
	chars_list = list(chars)
	for i in chars_list:
		json_file["notes"].append(BRAILLE_TABLE[i])

if __name__ == "__main__":
    text = input("歌詞を入力")
    romaji = convert_to_romaji(text)
    print(romaji)