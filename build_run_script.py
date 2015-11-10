import os, glob, itertools, collections
from src.wrangle import wrangle_text

GPU_CORES = [0,1,2,3]

args = {
    "num_layers" : 2,
    "dropout"    : 0.50,
    "rnn_size"   : 512,
    "max_epochs" : 30,
    "char_rnn_src" : "~/src/char-rnn",
    "local_dir"  : os.getcwd(),
    "eval_every" : 150,
}

print "Checking that all input data has been wrangled."

F_RAW = glob.glob("raw_input/*.txt")[:]
NAMES = map(wrangle_text, F_RAW)

os.system("mkdir -p logs")
os.system("mkdir -p output")

print "Found {} input files.".format(len(NAMES))

GPU_ITER = itertools.cycle(GPU_CORES)

cmd = "cd {char_rnn_src}; th train.lua -data_dir {local_dir}/input/{name}/ -num_layers {num_layers} -dropout {dropout} -rnn_size {rnn_size} -max_epochs {max_epochs} -gpuid {GPUID} -eval_val_every {eval_every} -checkpoint_dir {local_dir}/output/{run_name} | tee {local_dir}/logs/{run_name}.log"

SHELL_TXT = collections.defaultdict(list)

for k,name in zip(GPU_ITER,NAMES):
    args["GPUID"] = k
    args["name"]  = name
    args["run_name"] = "{name}_{rnn_size}_{dropout}".format(**args)
    os.system("mkdir -p output/{run_name}".format(**args))
    c = cmd.format(**args)
    SHELL_TXT[k].append(c)


for k in SHELL_TXT:
    f_swarm = "swarm_gpu_{}.sh".format(k)
    with open(f_swarm,'w') as FOUT:
        for line in SHELL_TXT[k]:
            FOUT.write(line+'\n')
    os.system('chmod u+x {}'.format(f_swarm,))

