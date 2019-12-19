# Machine_Learning
Auto-encoder를 이용한 Mnist 이미지 복원

아나콘다는 4.7.12 버전을 사용

파이썬은 3.7.5 버전을 사용

텐서플로우는 1.14.0 버전을 사용

## Mnist/data

  __`t10k-images-idx3-ubyte`__  테스트 셋 이미지입니다.

  __`t10k-labels-idx1-ubyte`__  테스트 셋 레이블입니다.

  __`train-images-idx3-ubyte`__ 훈련 셋 이미지입니다.

  __`train-labels-idx1-ubyte`__ 훈련 셋 레이블입니다.

  Mnist자필 숫자 데이터베이스에는 60,000개의 학습셋과 10,000개의 테스트셋이 있습니다.
  
  
  출처--http://yann.lecun.com/exdb/mnist/


## autoencoder_mnist.py

  autoencoder 파이썬 오픈소스 코드입니다.
  `hidden layer` 갯수와 `learning_rate`, `batch_size`, `display_step`등을 설정하였습니다.
 
## download.py, input_data.py
  
 메인코드에 필요한 라이브러리 입니다.
