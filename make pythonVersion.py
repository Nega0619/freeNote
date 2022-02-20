import clipboard
"""
conda                         4.11.0
conda-build                   3.21.7
conda-package-handling        1.7.3
얘네는 conda update conda 로 해결
"""


string1 = """
beautifulsoup4                4.6.0
datasets                      1.14.0
decorator                     4.4.2
"""

string2 ="""
cmake                         3.21.3
dlib                          19.22.1
face-recognition              1.3.0
face-recognition-models       0.3.0
glob2                         0.7
google-api-core               2.2.2
google-api-python-client      2.26.1
google-auth                   2.3.3
google-auth-httplib2          0.1.0
google-auth-oauthlib          0.4.6
google-cloud-vision           2.5.0
google-pasta                  0.2.0
googleapis-common-protos      1.53.0
googletrans                   3.0.0
"""

string3 = """
h11                           0.9.0
h2                            3.2.0
h3                            3.7.3
h5py                          3.1.0
httpcore                      0.9.1
httplib2                      0.20.2
httpx                         0.13.3
"""

string4 = """
imageio                       2.9.0
imageio-ffmpeg                0.4.5
imantics                      0.1.12
imbalanced-learn              0.8.1
imgaug                        0.4.0
"""

string5 = """
implicit                      0.4.8
importlib-metadata            4.8.2
importlib-resources           5.4.0
iopath                        0.1.9
ipykernel                     6.6.0
ipython                       7.28.0
ipython-genutils              0.2.0
ipywidgets                    7.6.5
itsdangerous                  2.0.1
"""

string6 = """
jsonpickle                    2.0.0
jsonschema                    4.2.1
jupyter-client                7.1.0
jupyter-core                  4.9.1
jupyter-desktop-server        0.1.3
jupyter-server                1.13.1
jupyter-server-proxy          3.2.0
jupyterlab-pygments           0.1.2
jupyterlab-widgets            1.0.2
"""
string7 = """
keras                         2.6.0
Keras-Applications            1.0.8
keras-ocr                     0.8.8
Keras-Preprocessing           1.1.2
matplotlib                    3.4.3
matplotlib-inline             0.1.3
matplotlib-venn               0.11.6
"""
string8 = """
numba                         0.53.1
numpy                         1.21.4
oauthlib                      3.1.1
"""
string9 = """
pandas                        1.3.3
pandocfilters                 1.5.0
parso                         0.8.3
pathspec                      0.9.0
patsy                         0.5.2
pexpect                       4.8.0
pickleshare                   0.7.5
Pillow                        8.3.2
pip                           21.3.1
pixellib                      0.7.1
"""

string10 = """
PyQt5                         5.15.6
PyQt5-Qt5                     5.15.2
PyQt5-sip                     12.9.0
regex                         2021.11.10
requests                      2.26.0
requests-file                 1.5.1
requests-oauthlib             1.3.0
"""

string11 = """
scikit-image                  0.18.3
scikit-learn                  1.0
scipy                         1.7.1
seaborn                       0.11.2
selenium                      4.0.0
statistics                    1.0.3.5
statsmodels                   0.13.0
summa                         1.2.0
"""

string12="""
tensorboard                   2.7.0
tensorboard-data-server       0.6.1
tensorboard-plugin-wit        1.8.0
tensorflow-addons             0.14.0
tensorflow-datasets           4.4.0
tensorflow-estimator          2.7.0
tensorflow-gpu                2.6.0
tensorflow-hub                0.12.0
tensorflow-metadata           1.5.0
"""

string13="""
tokenizers                    0.10.3
tomli                         1.2.2
torch                         1.9.1+cu111
torchaudio                    0.9.1
torchvision                   0.10.1+cu111
tornado                       6.1
tqdm                          4.62.3
"""

string14="""
uritemplate                   4.1.1
urllib3                       1.26.7
validators                    0.18.2
wget                          3.2
"""
string14="""
"""
string14="""
"""
string14="""
"""
string14="""
"""
string14="""
"""

splited_str = string5.split('\n')


result = ""
tobe_copy=""
for str in (splited_str[1:-1]):
    if(len(str)==0):
        continue
    else:
        result+=(str.split()[0]+'=='+str.split()[1])+' '

print('pip install '+result)
clipboard.copy('pip install '+result)
