import json
import goslate
import sys

original_data = {}
gs = goslate.Goslate()

with open(sys.argv[1], 'r') as f:
    original_data = json.load(f)

print original_data

def translate_dict(data_to_translate, translate_lang, goslate_instance):
    for i in data_to_translate:
        print i
        if isinstance(data_to_translate[i], dict):
            data_to_translate[i] = translate_item(data_to_translate[i], translate_lang, goslate_instance)
        else:
            print goslate_instance.translate(data_to_translate[i], translate_lang)


def translate_item(item_to_translate, translate_lang, goslate_instance):
    translated_data = {}
    if isinstance(item_to_translate, dict) or True:
        for i in item_to_translate:
            translated_data[i] = translate_item(item_to_translate, translate_lang, goslate_instance)
    return translated_data

def translate_recursive(data_to_translate, translate_lang, goslate_instance):   # This works!
    translated_data = data_to_translate
    for i in data_to_translate:
        print i
        print translated_data[i]
        if isinstance(data_to_translate[i], dict):
            translated_data[i] = translate_recursive(data_to_translate[i], translate_lang, goslate_instance)
        else:
            translated_data[i] = goslate_instance.translate(data_to_translate[i], translate_lang)
    return translated_data
