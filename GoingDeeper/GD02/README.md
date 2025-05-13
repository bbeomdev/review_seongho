# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 조성호
- 리뷰어 : 강희봉


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    ![image](https://github.com/user-attachments/assets/10b80b17-24a7-4a84-b53a-0f7adf2b1848)
    ![image](https://github.com/user-attachments/assets/7316aa14-9fb8-4466-a9db-d131aec019bc)
    ![image](https://github.com/user-attachments/assets/d587d8ae-2df1-476f-b35d-ced588992c91)
    ![image](https://github.com/user-attachments/assets/81a50ac4-e9c1-41ae-af23-afb5812ca012)
    ![image](https://github.com/user-attachments/assets/47e1da12-c581-434a-a4d2-aba51afa5736)
    - 5000, 10000, 20000, 전체단어 총 4가지 단어 수에 대해 8가지 머신러닝 기법을 적용하였으며 정확도 측면에서 SVM을 최고의 모델로 선정하였음
    - Vocabulary size에 따른 성능을 표와 그래프로 정리하고, 분석 내용을 작성하였음
    - 딥러닝 모델은 word index로 RNN 모델을 tfidf로 MLP 모델을 훈련하여 다른 모델들과 성능을 비교하고 분석하였음


- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - vocab size에 따른 모델 성능 비교 실험 이므로 vocab 사이즈와 모델을 정의하는 부분이 핵심 markdown block으로 잘 구분하여 표시
    ![image](https://github.com/user-attachments/assets/d0ed2bbe-6be3-40a1-86db-310f649fb06c)
    ![image](https://github.com/user-attachments/assets/825b5d2b-ef70-4ea2-8157-dab1d87f5521)

        
- [x]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - classification_report 로 각 클래스별 precision recall f1 을 확인
      ![image](https://github.com/user-attachments/assets/a24dfabf-f321-45c2-aaf0-9d1d005d02c1)
    - weighted F1 스코어를 비교
      ![image](https://github.com/user-attachments/assets/66d0e64d-f3d2-408d-be6d-79c29029fa60)
      
- [x]  **4. 회고를 잘 작성했나요?**
    - 실험에서 좋았던 점과 아쉬움 점을 작성하고 차 후 도움이 될 부분에 대해 작성함
        
- [x]  **5. 코드가 간결하고 효율적인가요?**
    - vocab 사이즈에 따른 실험이 위주라 코드가 그리 많지 않지만 코드 및 노트북이 깔끔하게 작성되었습니다.


# 회고(참고 링크 및 코드 개선)
base code를 완성하고 이미 실험이 진행된 상태에서 class 별 metric 을 확인해보면 좋았겠다라고 생각했었는데
실험별로 class 별 precision,recall,f1과 weighted F1 스코어를 확인 할 수 있어 좋았습니다. 
아쉬운 점은 class 별 metric 들은 분석에는 사용되지 않은 것 같아 약간 아쉬움이 있습니다. 
