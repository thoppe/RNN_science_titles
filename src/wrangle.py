import codecs
import collections
import glob
import os
import string
from unidecode import unidecode


keep_punc = "-:().?'=<>"
min_counts = 10

punc = ''.join([x for x in string.punctuation if x not in keep_punc])
presumed_codec = 'utf-8'

def wrange_text(f):
    
    name = os.path.basename(f).split('.txt')[0]
    os.system('mkdir -p input')
    os.system('mkdir -p input/{}'.format(name))

    f_out = os.path.join("input",name,"input.txt")
    if os.path.exists(f_out):
        print f, "already exists, skipping."
        return False
    
    print "Starting", name
    
    with codecs.open(f,'r',presumed_codec) as FIN:
        raw = FIN.read()
        
    rawstr = unidecode(raw)
    table = string.maketrans(punc, " "*len(punc))
    s = rawstr.translate(table)

    # Remove extra spaces from unidecode
    s = '\n'.join([' '.join(line.split())
                   for line in s.split('\n')])

    C = collections.Counter(s)

    # Remove all characters seen < min_counts
    low_counts = [key for key in C if C[key]<min_counts]
    print "Removing", low_counts
    
    for key in low_counts:
        s = s.replace(key,'')

    with open(f_out,'w') as FOUT:
        FOUT.write(s)

    return True


F_RAW = glob.glob("raw_input/*.txt")

for f in F_RAW:
    wrange_text(f)


