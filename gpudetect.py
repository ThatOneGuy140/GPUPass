import subprocess as sp;
import gpulist

def checkGPU():
    gpus = []
    #fuck you

    lspciOutput = sp.run('lspci -k | grep "NVIDIA"',shell=True,text=True,capture_output=True); #Run lspci -k
    lspciOutput = lspciOutput.stdout; #Convert output so i can actually use it

    #Filtering out unnescesary characters
    lspciOutput = lspciOutput.replace("]","");
    lspciOutput = lspciOutput.replace("[","");

    lspciOutput = lspciOutput.split(); #split the output into a list
    print(lspciOutput);

    for text in lspciOutput:
        if text in gpulist.list:
            gpus.append(text);
            (print(text,"Detected!"));

    print("GPUs found:",gpus);
    return gpulist;
