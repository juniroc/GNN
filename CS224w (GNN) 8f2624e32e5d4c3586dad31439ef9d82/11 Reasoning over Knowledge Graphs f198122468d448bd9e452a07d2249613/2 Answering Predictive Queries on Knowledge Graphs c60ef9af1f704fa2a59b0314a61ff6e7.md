# 2. Answering Predictive Queries on Knowledge Graphs

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled.png)

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%201.png)

- 1 장에서 다룬 제한으로 인해 수행하는 것이 Predictive Queries
- 그래프를 완성하지 않은 상태에서 주어진 query (head, relation)에 대한 tail을 찾는 작업
    
    → KG Embedding 을 활용
    
    - 그중 TransE

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%202.png)

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%203.png)

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%204.png)

- TransE 를 학습 할 수 있음

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%205.png)

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%206.png)

- 위 질문 `어떤 약이 숨가쁨을 야기하고, ESR2 단백질과 연관된 질병을 다루는가?`

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%207.png)

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%208.png)

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%209.png)

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%2010.png)

- 만약 링크 하나가 missing edges 인경우 우리는 `Fulvestrant` 는 찾을 수 없었을 것

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%2011.png)

- 어떻게 ESR2 가 `Breast Cancer`과 관련있다고 생각할 수 있는지?
→ ESR2와 상호작용하는 `BRCA1` 과 `ESR1` 이 둘다 `Breast Cancer` 과 연관되어있어서 추론할 수 있음

![Untitled](2%20Answering%20Predictive%20Queries%20on%20Knowledge%20Graphs%20c60ef9af1f704fa2a59b0314a61ff6e7/Untitled%2012.png)

- 중간 node 들은 어떻게 latent space 로 나타낼 수 있는지?
→ 다음시간에 계속