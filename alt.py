import os
import configparser

def main():
    new_alt = find_alt_file()
    alt     = load_alt_file()
    
    if not new_alt: compile(alt)

def load_alt_file():
    alt = configparser.RawConfigParser(allow_no_value=True)
    alt.optionxform = str
    alt.read(f'{os.getcwd()}/.alt')
    alt.sections()
    return alt

def make_alt_file():
    alt = open(".alt", "a")
    alt.write("[CLI]\ncl\n\n")
    alt.write("[VERSION]\nc++20\n\n")
    alt.write("[NAME]\nout.exe\n\n")
    alt.write("[ARGS]\n/EHcs\n/MP\n/nologo\n\n")
    alt.write("[FILES]\n\n")
    alt.write("[INCLUDES]\n\n")
    alt.write("[LIBS]\n\n")
    alt.write("[DEFINES]\n\n")
    alt.close()

def find_alt_file():
    if not os.path.exists(f'{os.getcwd()}/.alt'):
        make_alt_file()
        return True

def compile_add(alt, target, compile):
    for targ in alt[target]:
        compile += targ + " "
    return compile

def compile_prefix(alt, prefix, target, compile):
    for targ in alt[target]:
        compile += prefix + targ + " "
    return compile

def compile(alt):

    compile = ""
    compile = compile_add   (alt, "CLI"            , compile)
    compile = compile_add   (alt, "ARGS"           , compile)
    compile = compile_prefix(alt, "/std:","VERSION", compile)
    compile = compile_prefix(alt, "/Fe","NAME"     , compile)
    compile = compile_add   (alt, "FILES"          , compile)
    compile = compile_prefix(alt, "/I","INCLUDES"  , compile)
    compile = compile_add   (alt, "LIBS"           , compile)
    compile = compile_prefix(alt, "/D","DEFINES"   , compile)
    os.system("cls")
    os.system(compile)

main()