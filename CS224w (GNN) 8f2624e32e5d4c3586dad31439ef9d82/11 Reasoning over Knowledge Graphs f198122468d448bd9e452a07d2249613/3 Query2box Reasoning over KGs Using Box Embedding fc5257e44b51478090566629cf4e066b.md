# 3. Query2box: Reasoning over KGs Using Box Embeddings

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%201.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%202.png)

- ex) Fulvestrant 약품 관련된 것들은 모두 하나의 박스 내부에 가깝게 임베딩시키고 싶음

## 4-1. 임베딩 벡터

- query2box에서 노드들은 임베딩 공간에 맵핑
- query(entity + relation)은 박스의 형태로 임베딩 공간에 표현
    - Ex) 
    Fulvestrant(anchor node)의 adverse event(relation)이 1)Short of Breath 2)Kidney Infection 3) Headache(tails) 일때, 아래 박스 같이 query를 표현할 수 있다.

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%203.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%204.png)

- Box Embedding을 하기 위해 알아야 할 것들
    - Entity Embeddings
    - Relation Embeddings (Projection Opoerator)
    - Intersection Operator

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%205.png)

- projection operator
    - relation embedding에 따라 주어진 박스를 이동, 크기를 줄이거나 늘리는 역할하는 연산자
    - 즉, 현재의 박스와 relation을 입력으로 받아 이동된 박스 리턴
- Cen(q') : 박스의 중심을 이동
- Off(q') : 박스 크기 변화

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%206.png)

1. anchor node 임베딩 벡터 표현
    - anchor node 임베딩 벡터는 오른쪽에서 볼 수 있듯이 크기가 0인 박스로 표현
    - 이때 박스이기 때문에 projection operator를 통해 크기가 늘어나거나 줄어들수도 있고, 위치가 변화

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%207.png)

1. (ESR2,Assoc)에 대한 projection operator 수행
- anchor 노드에서 Assoc이라는 relation 임베딩 벡터에 해당하는 projection operator를 수행
- 그 결과 오른쪽 그림과 같이 tail에 해당하는 노드 집합이 모두 안에 들어가는 사각형으로 위치와 크기가 변화

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%208.png)

1. (TreatedBy)에 대한 projection operator 수행
- 새로운 relation에 맞는 tail이 박스 안에 모두 들어오도록 기존의 박스에서 새로운 박스로 중심과 크기가 변화

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%209.png)

1. Short of Breath 에 관련된 임베딩 박스 생성

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2010.png)

1. 서로 교차하는 부분 박스 임베딩

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2011.png)

- 새로운 박스는 기존 박스들의 중심과 가까워야함
- 박스 사이즈는 기존 박스중 가장 작은 값보다 작아야 함

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2012.png)

- Center 구하는 공식
1. 각 박스의 중심 벡터가 임의의 함수 *f(cen)*을 통과하고, 소프트맥스 함수를 통과하여 가중치 벡터 *wi 가 됨*
2. 가중치 벡터 *wi*와 실제 중심을 나타내는 벡터를 아다마르 곱하여 가중합

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2013.png)

- offset 구하는 공식
- sigmoid 등을 쓰는데 → 기존보다 작은 크기를 써야하므로

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2014.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2015.png)

- 박스 외부 것들도 사용하는 경우
    - 거리를 산출하는 함수
        - 박스 외부부터 경계면까지의 거리는 그대로 사용
        - 박스 내부의 거리는 가중치를 주어 좀 더 작게 측정

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2016.png)

- and-or queries 는 처리가 가능한가?

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2017.png)

- 불가능하지만
→ 높은 차원의 임베딩이 필요로 함 (불가능하다 볼 수 있음)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2018.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2019.png)

- union 인 경우 
→ 두가지를 한박스로 묶어서

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2020.png)

- 다음과 같이 박스형태로 바꿀 수 없는 경우는 어떻게하나?
→ 불가능하다 → 1차원 더 넓혀주어야함

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2021.png)

- 약 15000 차원이 필요함;;
→ 다른 방법은 없는가?

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2022.png)

- 위 사진처럼 변환해주면 낮은 차원에서도 가능
- `(*a*∪*b*)∩*c` ⇒* `(*a*∩*c*)∪(*a*∩*b*)` 로 이야기할 수 있음

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2023.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2024.png)

- 즉 v 의 conjunctive query 중 하나가 q 인 경우 v 의 대답은 q가 될 수 있고,
- v 의 conjunctive query 중 하나가 q 와 가깝다면 v 는 q 와 embedding space 에서 가까울 수 있음

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2025.png)

### query2box 과정을 정리하면

1. and 연산을 모두 수행하여 or 연산으로만 이루어진 query들을 만들어 낸다.
    
    ![https://media.vlpt.us/images/stapers/post/38270530-8124-46d4-a050-aa4008e50fc0/image.png](https://media.vlpt.us/images/stapers/post/38270530-8124-46d4-a050-aa4008e50fc0/image.png)
    
2. 각 query의 임베딩을 구한다(박스를 구한다)
3. 각 query와 노드 *v*와의 거리를 구한다.
4. 3에서 구한 거리 중 가장 최소의 거리를 최종 거리로 선택한다.
5. 최종 점수 *fq*(*v*) = −*dbox*(*q*,*v*)를 구한다.

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2026.png)

- 학습은 단순하게 correct answer에 대해 fq score를 늘리고 negative answer에 대해 fq score를 줄이는 것

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2027.png)

- 여기서 예시로 버락 오바마(anchor node), 국적(relation), 미국(answer node), 한국(wrong answer node)
1. 랜덤하게 query *q*를 학습 그래프 *G_train*에서 추출하고, 해당 query의 정답 노드 와 오답 노드를 추출
2. query *q*를 intersection operator를 이용해 임베딩(최종 박스를 구한다.)
3. 정답노드와 오답노드에 대한 스코어 *f_q*(*v*), *f_q*(*v*′)를 구한다.
4. *f_q*(*v*)를 최대화하고, *f_q*(*v*′)를 최소화하도록 손실함수를 구성

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2028.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2029.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2030.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2031.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2032.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2033.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2034.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2035.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2036.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2037.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2038.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2039.png)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2040.png)

- 1번째 anchor 노드에서 시작
- 현악기 연주자

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2041.png)

- 1번째 relation 이동
- 모든 정답 노드가 박스 안으로 들어와 정답률이 100% 가됨

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2042.png)

- 2번째 relation 이동
- 일부 정답 노드가 밖으로 빠져나옴 정답률이 소폭 낮아짐

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2043.png)

- 2번째 anchor 노드 시작
- 남성

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2044.png)

- 3번째 relation 이동
- 이때, 남자 연주자가 무척 많다보니, 당연하게도 박스가 커지고 임베딩 공간에서도 크게 표시된 것을 볼 수 있다.

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2045.png)

- 3번과 5번 박스를 Intersection 함수에 삽입
- 최종 결과 및 정답률 출력 (이전보다 올라감)

![Untitled](3%20Query2box%20Reasoning%20over%20KGs%20Using%20Box%20Embedding%20fc5257e44b51478090566629cf4e066b/Untitled%2046.png)