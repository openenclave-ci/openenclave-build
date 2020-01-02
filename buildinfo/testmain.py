import os 

if __name__ == "__main__":

    # Get the package list for the base system (thoughtfully provided in the Dockerfile)
    f = open("/tmp/pkglist.base", "r")
    lines = f.readlines()

    # Strip cruft from dpkg so we only get a list of installed package dependencies
    base_pkg_list = [ i for i in lines if i and i[0] == 'i' ]

    lines = os.popen('dpkg -l').read().split('\n')
    current_pkg_list = [ i for i in lines if i and i[0] == 'i' ]

    pkg_list = current_pkg_list.copy()
    for i in current_pkg_list:
       for j in base_pkg_list:
            if i.split()[1] == j.split()[1]:
                print("removing "+i.split()[1])
                pkg_list.remove(i)
   
    f = open("/output/pkglist.installed", "w")
    for pkg in pkg_list:
        print(pkg+"\n", file=f)

    f.close()
    
