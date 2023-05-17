# Co. Meet-REST

[Co. Meet REST전환 및 Next JS이식 프로젝트](https://github.com/VinylStage/CoMeet)

## Start Routine

### 가상환경 재구성

    poetry env use py

#### window기준

    source .venv/scripts/activate

#### mac은 해당 path를 찾아주어 적용하면 됨

    poetry env info --path

### 종속패키지 설치

#### requirements사용시

    pip install -r requirements.txt

#### poetry 사용시

    poetry update package

    poetry install

#### requirements에서 poetry로 이동시

    cat requirements.txt | grep -E '^[^# ]' | cut -d= -f1 | xargs -n 1 poetry add

#### poetry에서 requirements로 이동시

    poetry export -f requirements.txt --output requirements.txt

### 시크릿키 발급

    py -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

https://djecrety.ir/

    touch secrets.json

    {
      "SECRET_KEY": "해당 키"
    }

#### db.sqlite3에 migrate

    py manage.py migrate

#### 이슈체크

    py manage.py check

#### 관리자 계정생성 및 서버테스트

    py manage.py createsuperuser

    py manage.py runserver

---

# Project Purpose

이 프로젝트는 개인적인 DRF및 Next JS학습을 위해 제작되었습니다

## Usage Language & FrameWork

Backend - Python, Django Rest Framework

Frontend - React, Next JS

## Usage Management Method

requirements.txt

poetry

json
