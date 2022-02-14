# 3. Knowledge Graph Completion: TransE, TransR, DistMul, ComplEx

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled.png)

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%201.png)

- (head, relation)이 주어졌을 때 누락된 tail을 예측하는 것
- 누락된 tail을 찾음으로써 (head, relation, tail)을 만들어 edge를 만듦
- 이러한 측면에서 볼 때 link prediction task와 다름

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%202.png)

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%203.png)

- KG Representation
    - KG에서 Edge는 (h, r, t)로 표현
    - h = head, r = relation, t = tail

## Key Idea

- entity와 relation을 embedding space로 모델링하는 것
- node embedding 으로 shallow embedding 이용함
- GNN을 이용하진 않지만 원한다면 이용 가능함
- (h, r, t)가 주어졌을 때, (h, r) 임베딩과 가까운 (t) 임베딩 찾는 것
    - (h, r) 임베딩하는 방법?
    - 가까움을 정의하는 방법?

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%204.png)

- TransE
- h + r 이 t와 유사하면 될 것
- Scoring function이 h와 t의 가까움을 정의하는 함수
- word2vec와 비슷한 개념
ex) 
h = '나', r = 'Nationality' 이면
⇒ t = 'Korea' 가 되어야 함

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%205.png)

- TransE Learning Algorithm

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%206.png)

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%207.png)

- TransE
    - Symmetric Relation을 표현할 수 없음
    → h + r = t 일 때  t + r = h 가 성립되지 않음 (대칭이 안됨)

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%208.png)

- TransE
    - AntiSymmetric Relation 표현 가능
        
        ⇒ h + r = t 이지만, t + r ≠ h 임
        
    - 위와 같은 말

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%209.png)

- TransE
    - Inverse Relation 표현 가능
    - r_1 = -r_2 인 경우

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2010.png)

- TransE
    - Composition Relation 표현 가능
    - r_1 + r_2 = r_3 인 경우
    - r_1(x, y) | r_2(y, z) = r_3(x,z)

### TransE 의 한계

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2011.png)

- TransE
    - Symmetric Relation을 표현할 수 없음
    → h + r = t 일 때  t + r = h 가 성립되지 않음 (대칭이 안됨)
    - r = 0 인 경우(h =t)만 가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2012.png)

- TransE
    - 1-to-N Relation을 표현할 수 없음.

## TransR

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2013.png)

## 2) TransR

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2014.png)

- TransR
    - entity를 임베딩하는 공간 / relation을 임베딩하는 공간을 나눔
    - 위 두개를 연결짓기 위해서 projection matrix을 사용

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2015.png)

- Symmetric Relation 표현 가능
- TransR은 entity 임베딩 공간과 relation 임베딩 공간이 다르므로

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2016.png)

- Antisymmetric Relation 표현 가능
    
    

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2017.png)

- 1-to-N Relation 표현 가능
    - embedding 표현이므로
    

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2018.png)

- Inverse Relation 표현 가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2019.png)

- Composition Relation 표현 불가능
    - entity의 임베딩 공간이 다르므로 불가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2020.png)

- h, r, t의 내적과 sum으로 표현

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2021.png)

- h * r과 t 사이의 cosine similarity로 확인
→ 각도가 가까울 수록 좋음

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2022.png)

- 1-to-N Relation 표현 가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2023.png)

- Symmetric Relation 표현 가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2024.png)

- Antisymmetric Relation 표현 불가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2025.png)

- Inverse Relation 표현 불가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2026.png)

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2027.png)

- entity와 relation을 Complex vector space(스칼라를 복소수로 확장하는 것)에 임베딩
→ Distmult와 비슷

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2028.png)

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2029.png)

- Antisymmetric Relation 표현 가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2030.png)

- Symmetric Relation 표현 가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2031.png)

- Inverse Relation 표현 가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2032.png)

- Composition & 1-to-N Relation 표현 불가능

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2033.png)

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2034.png)

![Untitled](3%20Knowledge%20Graph%20Completion%20TransE,%20TransR,%20DistM%200fa926e392dc41c9b7fe3ef28ea9eb12/Untitled%2035.png)