import subprocess,sys
def install(package):
    subprocess.call([sys.executable, "-m","pip","--disable-pip-version-chec","-q", "install", package])
install('PyDictionary')

from PyDictionary import PyDictionary

a,b=PyDictionary(),input('word that you need meaning of: ') or "God"
print(f" Meaning of {b} 👇👇👇 : \n\n {a.meaning(b)} \n\n\n\n Synonym of {b} 👇👇👇 : \n\n {a.synonym(b)} \n\n\n\n Antonym of {b} 👇👇👇 : \n\n {a.antonym(b)} \n\n")