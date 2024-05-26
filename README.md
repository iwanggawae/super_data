# **Super Data Generator**
Simple Python script to randomly generate questionnaire data with customizable number of participants and questions. The resulting data will be saved in Excel_ format (`hasil_kuesioner.xlsx`)

_Skrip Python sederhana untuk menghasilkan data kuesioner secara acak dengan jumlah partisipan dan pertanyaan yang dapat disesuaikan. Data yang dihasilkan akan disimpan dalam format Excel_ (`hasil_kuesioner.xlsx`).


## **Features**
- Custom number of questions
- Custom number of participants
- (NEW) Auto data summary
- (NEW) Auto Reliability test result (Cronbach's Alpha)
- Automatically export data to Excel

## **Requirements:**
- Python3
- pandas
- termcolor
- tqdm
- openpyxl
- pingouin

## Installation

#### Terminal/Termux
1. Repository
```sh
git clone https://github.com/iwanggawae/super_data
```
2. Open Directory
```sh
cd super_data
```
3. Requirements Installation
```sh
python3 -m pip install -r requirements.txt
```
4. Run
```sh
python3 sd.py
```
