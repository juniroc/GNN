# 3. Embedding Entire Graphs

## 전체 그래프 임베딩

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled.png)

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%201.png)

- 기존 노드 임베딩들의 합을 그래프 임베딩으로 이용

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%202.png)

- 가상(virtual) 노드를 만들어 해당 지역을 대표하는 그래프 임베딩으로써 이용

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%203.png)

- 노드 번호나 이름에 상관없이 먼저 방문한 것을 1 그 다음을 2 ...
- 같은 이름의 노드에 방문했다면 기존에 방문했던 순서를 숫자로 넣어줌

```jsx
Anonymous Walk는 random walk를 하는데 어느 node를 지나왔느냐가 아닌, 
지나온 순서를 고려하는 random walk입니다. 
random walk를 진행하고 그 발자취의 순서(index)를 Anonymous Walk라고 합니다.
Anonymous Walk의 결과로 embedding하는 것을 Anonymous Walks Embeddings이라고 합니다.

이 방법은 length에 따라 walk수가 폭발적으로 늘어납니다.
```

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%204.png)

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%205.png)

- 3개의 스텝에서 경우의 수

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%206.png)

- 만약 l = 3 만큼의 스텝을 이용한다면, 그래프는 5-dimension vector 로 만들 수 있음.

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%207.png)

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%208.png)

- s.t == step

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%209.png)

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%2010.png)

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%2011.png)

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%2012.png)

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%2013.png)

 

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%2014.png)

- 임베딩을 이용해 할 수 있는 작업들

![Untitled](3%20Embedding%20Entire%20Graphs%203284b154207b473e86c31688ba9eaacd/Untitled%2015.png)