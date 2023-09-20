import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url")
    return parser


urls = [
    "https://img3.akspic.ru/previews/9/6/1/9/6/169169/169169-ty_zasluzhivaesh_vsyacheskogo_schastya-schaste-strah-voda-polety_na_vozdushnom_share-x750.jpg",
    "https://img3.akspic.ru/previews/5/6/6/1/4/141665/141665-lyubov-peyzash-nebo-oblako-motivaciya-x750.jpg",
    "https://img3.akspic.ru/previews/6/3/5/8/98536/98536-rastitelnost-priroda-platezh-rastenie-velosport-x750.jpg",
    "https://img2.akspic.ru/previews/3/9/6/2/3/132693/132693-novyj_god-polnoch-noch-ded_moroz-den_novogo_goda-500x.jpg",
    "https://img3.akspic.ru/previews/2/1/8/7/87812/87812-arhitektura-voda-kitajskij_novyj_god-novyj_god-nebo-x750.jpg",
]

if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    urls.append(namespace.url)
