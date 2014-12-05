import json
import goslate
import argparse
from collections import OrderedDict

original_data = {}
gs = goslate.Goslate()

parser = argparse.ArgumentParser()

parser.add_argument("infile",  help="This is the input translation file.")
parser.add_argument("targetlang", help="The language to translate to.")
parser.add_argument(
    "-o", "--outfile", help="The file to save the translation in.")
parser.add_argument("-s", "--sourcelang", default="en",
                    help="The language the input file is in (default: en).")
parser.add_argument("-i", "--indent", type=int, nargs='?', const=1,
                    help="Specify the indent level of the outputted JSON file "
                    "(default: 2). If not specified the output file "
                    "will not extra whitespace.")

args = parser.parse_args()

print args


def translate_recursive(data_to_translate, translate_lang, input_lang, goslate_instance):
    translated_data = data_to_translate
    for i in data_to_translate:
        if isinstance(data_to_translate[i], dict):
            translated_data[i] = translate_recursive(
                data_to_translate[i], translate_lang, input_lang, goslate_instance)
        else:
            translated_data[i] = goslate_instance.translate(
                data_to_translate[i], translate_lang, input_lang)
    return translated_data


with open(args.infile, 'r') as f:
    original_data = json.load(f, object_pairs_hook=OrderedDict)

print "The input data is:"
print original_data

print "The translated data is:"
translated_data = translate_recursive(
    original_data, args.targetlang, args.sourcelang, gs)
print translated_data

if "outfile" in args:
    with open(args.outfile, 'w') as f:
        json.dump(translated_data, f, indent=args.indent)
