from colorama import Fore
import subprocess
import platform
import distro
import time
import os
import re

# Functions
def get_uptime():
    return os.popen('uptime -p').read()[:-1]

def get_os():
    return platform.system() + " " + platform.release()

def get_de():
    desktop_environment = 'generic'
    if os.environ.get('KDE_FULL_SESSION') == 'true':
        desktop_environment = 'kde'
    elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
        desktop_environment = 'gnome'
    else:
        try:
            info = getoutput('xprop -root _DT_SAVE_MODE')
            if ' = "xfce4"' in info:
                desktop_environment = 'xfce'
        except (OSError, RuntimeError):
            pass

    return desktop_environment

def get_screenres():
    return os.popen("xrandr  | grep \* | cut -d' ' -f4").read()[:-1]

def get_gpu():
    return os.popen('GPU=$(lspci | grep VGA | cut -d ":" -f3);RAM=$(cardid=$(lspci | grep VGA |cut -d " " -f1);lspci -v -s $cardid | grep " prefetchable"| cut -d "=" -f2);echo $GPU $RAM').read()[:-1]

def get_processor():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "", line,1)
    
    return "Undetected"

# Main Entry
def main():
    linux_distro = distro.name()
    os_str = f"OS: {get_os()}"
    uptime_str = f"Uptime: {get_uptime()}"
    de_str = f"Desktop Environment: {get_de()}"
    screenres_str = f"Screen Resolution: {get_screenres()}"
    processor_str = f"CPU: {get_processor()}"
    gpu_str = f"GPU: {get_gpu()}"
    if 'pop' in linux_distro.lower():
        print(Fore.CYAN + f"""


            ←←←←←←←←←←←              ╠════════════════════ ROGUE FETCH ════════════════════════╣
        ←←←←←←←←←←←←←←←←←←←                                   
      ←←←←←←    ←←←←←←←←←←←←←                                                                 
    ←←←←←         ↖←←←←←←←←←←←←            {os_str}                                           
   ←←←←     ←←      ←←←←←←←←←←←←                                                              
 ↖←←←←←     ←←←     ←←←←←←←←←←←←←↖         {uptime_str}                                                      
 ←←←←←←←     ←←←    ←←←    ↖←←←←←←                                                            
←←←←←←←←←     ←↖   ↖←←↖    ←←←←←←←←        {de_str}
←←←←←←←←←←        ←←←←    ↖←←←←←←←←
←←←←←←←←←←←    ↖←←←←←←   ↖←←←←←←←←←        {screenres_str}
←←←←←←←←←←←←    ←←←←←←  ←←←←←←←←←←←
←←←←←←←←←←←←←    ←←←←←↖←←←←←←←←←←←←        {processor_str}
 ←←←←←←←←←←←←←   ↖←←←↖ ←←←←←←←←←←← 
 ↖←←←←←←←←←←←←←  ←←←←  ←←←←←←←←←←↖         {gpu_str}
   ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←     
    ←←←←                   ←←←←     ╠═════════════════════════════════════════════════════════╣
      ←←←←←←←←←←←←←←←←←←←←←←←      
        ←←←←←←←←←←←←←←←←←←←        
            ←←←←←←←←←←←            
  
        """)
    
    if 'arch' in linux_distro.lower():
        print(Fore.BLUE + f"""


            ↘↘↘↘↘↘↘↘↘↘↘              ╠════════════════════ ROGUE FETCH ════════════════════════╣
        ↘↘↘↘↘↘↘↘↘ ↘↘↘↘↘↘↘↘↘             
      ↘↘↘↘↘↘↘↘↘↘   ↘↘↘↘↘↘↘↘↘↘        
    ↘↘↘↘↘↘↘↘↘↘↘     ↘↘↘↘↘↘↘↘↘↘↘             {os_str}
   ↘↘↘↘↘↘↘↘↘↘↘↓      ↘↘↘↘↘↘↘↘↘↘↘            
  ↘↘↘↘↘↘↘↘↘↘↘↘       ↓↘↘↘↘↘↘↘↘↘↘↘           {uptime_str}
 ↘↘↘↘↘↘↘↘↘↘↘↘         ↘↘↘↘↘↘↘↘↘↘↘↘ 
↘↘↘↘↘↘↘↘↘↘↘↘           ↘↘↘↘↘↘↘↘↘↘↘↘         {de_str}
↘↘↘↘↘↘↘↘↘↘↘             ↘↘↘↘↘↘↘↘↘↘↘
↘↘↘↘↘↘↘↘↘↘      ↘↘↘      ↘↘↘↘↘↘↘↘↘↘         {screenres_str}
↘↘↘↘↘↘↘↘↘      ↘↘↘↘↘      ↘↘↘↘↘↘↘↘↘
↘↘↘↘↘↘↘↘      ←↘↘↘↘↘↓    ↘ ↘↘↘↘↘↘↘↘         {processor_str}
 ↘↘↘↘↘↘        ↘↘↘↘↘↙       ↘↘↘↘↘↘          
  ↘↘↘↘    ↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘    ↘↘↘↘           {gpu_str}
   ↘↘ ↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘ ↘↘   
    ↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘     ╠═════════════════════════════════════════════════════════╣  
      ↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘      
        ↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘↘        
            ↘↘↘↘↘↘↘↘↘↘↘            
        """)
    
    if 'debian' in linux_distro.lower():
        print(Fore.RED + f"""



            →→→→→→→→→→→            ╠════════════════════ ROGUE FETCH ════════════════════════╣        
        →→→→→→→→→→→→→→→→→→→        
      →→→→→→→→→→→→→→→→→→→→→→→      
    →→→→→→→→→→↘      →→→→→→→→→→             {os_str}    
   →→→→→→→→↘    →→→→→    →→→→→→→   
  →→→→→→→→  ↙→→→→→→→→→→   →→→→→→→           {uptime_str}
 →→→→→→→→  →→→→→→→→→→→→→  ↙→→→→→→→ 
→→→→→→→→  →→→→→→↓→→→→→→→→ →→→→→→→→→         {de_str}
→→→→→→→→ →→→→→→ →→→→→→→→→ →→→→→→→→→
→→→→→→→→ →→→→→→ →→→→→→→→ →→→→→→→→→→         {screenres_str}
→→→→→→→→ ↓→→→→→→↙↘→→→→→ →→→→→→→→→→→
→→→→→→→→→ ↘→→→→→→→ →→→→→→→→→→→→→→→→         {processor_str}
 →→→→→→→→  →→→→→→→→→→→→→→→→→→→→→→→ 
  →→→→→→→→→ →→→→→→→→→→→→→→→→→→→→→           {gpu_str}
   →→→→→→→→→  →→→→→→→→→→→→→→→→→→   
    →→→→→→→→→→→ →→→→→→→→→→→→→→→    ╠═════════════════════════════════════════════════════════╣  
      →→→→→→→→→→→→→→→→→→→→→→→      
        →→→→→→→→→→→→→→→→→→→        
            →→→→→→→→→→→            

        """)


# Entry Call
if __name__ == "__main__":
    main()
