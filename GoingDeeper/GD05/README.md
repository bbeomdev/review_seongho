# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 조성호
- 리뷰어 : 김영숙


# PRT(Peer Review Template)
- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - hyperparamer별로 챗봅응답 결과를 확인하였습니다
        - ![image](https://github.com/user-attachments/assets/13dcff4c-88bc-46bb-a331-5ad30a6e5aa7)

    
- [X]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - hyperparametr를 설정하고, 설정된 조합으로 자동 train을 하도록 함수를 구성하였습니다. 
        - ![image](https://github.com/user-attachments/assets/a65da3a5-1d55-4295-8b07-6077b64c38c4)

        
- [X]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    -  평가지표로 perplexity를 사용하였습니다.
    - ![image](https://github.com/user-attachments/assets/4a4efde8-af34-4bcc-903b-21a50338260f)
        
- [X]  **4. 회고를 잘 작성했나요?**
    - 데이타 증강, nlp 모델 리서치 사용에 대한 회고 및
    - 팀내 다른 증강법에 대한 시험 결과를 비교했습니다. 
        - ![image](https://github.com/user-attachments/assets/82ab03a8-8b8f-4ee0-803f-7a18d6aa8a59)

        
- [X]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - train 함수에 옵션들을 설정하여 튜닝할 수 있는 함수를 구성했습니
        - ![image](https://github.com/user-attachments/assets/21d97ff0-20a8-4701-988c-7e2a4f4f29a5)



# 회고(참고 링크 및 코드 개선)
```
- 데이타 증강을 backtrace를 사용함.
- nllb 모델을 리서치하여 사용 
```
