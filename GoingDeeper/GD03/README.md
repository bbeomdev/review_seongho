# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 조성호
- 리뷰어 : 강희봉


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 워드임베딩의 most_similar() 메소드 결과
    ![image](https://github.com/user-attachments/assets/d137c141-6032-4bfc-8a77-57cfbfa6288d)    
    - 영화 구분, 장르별로 target, attribute에 대한 대표성있는 단어 셋을 생성 ( 여러세트중 LSA를 이용한 세트 일부 캡쳐)   
    ![image](https://github.com/user-attachments/assets/002b92ed-ce72-4cb8-bd81-65dc9ef091ae)    
    - WEAT score 계산 및 시각화 ( LSA 이용 시각화 부분 캡쳐 )   
    ![image](https://github.com/user-attachments/assets/66d26b74-6ede-43ea-b5a8-8d8ffe5ccf71)    
    ![image](https://github.com/user-attachments/assets/9e14fb08-de40-48fb-a9ee-2ad21375ab4a)    


- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 핵심은 단어 추출을 TF-IDF가 아닌 LSA로 변경한 부분으로 판단했습니다. 주석을 달아두어 이해하기 편했습니다.
    ![image](https://github.com/user-attachments/assets/afbaa19b-d93a-4821-8676-3481794e96da)

        
- [x]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - TF-IDF 에서 중복을 일부만 허용한 케이스와 LSA로 추출한 케이스를 추가했습니다.
    ![image](https://github.com/user-attachments/assets/203feb98-b351-4756-acb6-ab1754774119)

        
- [x]  **4. 회고를 잘 작성했나요?**
    - 어려웠떤 점과 고민한 부분 그리고 배운 부분과 앞으로 고려할 사항을 잘 정리하였습니다.
        
- [x]  **5. 코드가 간결하고 효율적인가요?**
    - 간결하고 보기 편하게 작성되었습니다. 2번 항목 캡쳐 참조


# 회고(참고 링크 및 코드 개선)
- 시간이 없어 TF-IDF를 진행하지 못헸는데 LSA로 진행한 결과를 확인해 볼 수 있어서 좋았습니다.
- TF-IDF에서 편향성이 강하면서 잘못되었다고 생각되었던 다큐멘터리와 멜로로맨스 결과를 확인해보니 확실히 TF-IDF보다 LSA가 나은 결과를 보인다고 판단됩니다.
- 리뷰 시간에는 언급했던것 같은데 노트북에도 TF-IDF의 아쉬운 부분과 그것을 극복하기 위해 LSA를 선택한 이유 그리고 결과가 선택한 이유와 맞는지 등을 기록했으면 더 좋았을것 같습니다.
