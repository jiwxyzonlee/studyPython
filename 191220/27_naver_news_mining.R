### 뉴스 데이터 텍스트 마이닝
## 텍스트 마이닝 준비하기
# 패키지 설치하기
install.packages("rJava")
install.packages("memoise")
install.packages("KoNLP")

# 패키지 로드하기
library(KoNLP)
library(dplyr)

# 사전 설정하기
useNIADic()

## 데이터 준비하기
# 데이터 불러오기
#txt <- readLines("c:/crawl/news.txt")
csv <- read.csv("c:/crawl/news.csv", header = F)
txt <- csv$V3
head(txt)
length(txt)

# 특수문자 제거하기
install.packages("stringr")
library(stringr)

txt <- str_replace_all(txt, "\\W", " ")
head(txt)

## 가장 많이 사용된 단어 알아보기
# 명사 추출하기
nouns <- extractNoun(txt)
head(nouns)

# 추출한 명사 list를 문자열 벡터로 변환, 단어별 빈도표 생성하기
wordcount <- table(unlist(nouns))
head(wordcount)
tail(wordcount, 20)

# 데이터 프레임으로 변환하기
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
head(df_word)
tail(df_word)
str(df_word)

# 변수명 수정하기
df_word <- rename(df_word, 
                  word=Var1, 
                  freq= Freq)
tail(df_word)

# 두 글자 이상 단어 추출하기
df_word <- filter(df_word, nchar(word) >= 2)

# 빈도 순으로 정렬한 후 상위 20개 단어 추출하기
top_20 <- df_word %>% arrange(desc(freq)) %>% head(20)
head(top_20)

# 막대 그래프 그리기
library(ggplot2)
library(ggthemes)

ggplot(data = top_20, aes(x=word, y=freq, fill=word)) +
  geom_bar(stat = "identity") +
  geom_text(aes(label=freq), vjust=-0.3)  #빈도 표시

order <- arrange(top_20, freq)$word       #빈도 순서 변수 생성하기
ggplot(data = top_20, aes(x=word, y=freq, fill=word)) +
  geom_col() +                            #막대그래프(x축,y축을 모두 설정)
  scale_x_discrete(limit=order) +         #빈도순으로 막대 정렬
  #ylim(0, 50) +                           #y축의 범위 지정
  coord_flip() +                          #x축과 y축의 구성을 뒤집어 표현
  geom_text(aes(label=freq), hjust=-0.3)  #빈도 표시


## 워드 클라우드 만들기
# 패키지 설치/로드 하기
install.packages("wordcloud")
library(wordcloud)
library(RColorBrewer)

# 단어 색상 목록 만들기
pal <- brewer.pal(8, "Dark2")      

# 난수 고정하기
set.seed(1234)

# 워드 클라우드 만들기
wordcloud(words = df_word$word,    #단어
          freq = df_word$freq,     #빈도
          min.freq = 2,            #최소 단어 빈도
          max.words = 200,         #표현 단어 수
          random.order = F,        #고빈도 단어 중앙 배치
          rot.per = .1,            #회전 단어 비율
          scale = c(4, 0.3),       #단어 크기 범위
          colors = pal)            #색상 목록

# 단어 색상 바꾸기
pal <- brewer.pal(9, "Blues")[5:9] #색상 목록 생성
set.seed(1234)                     #난수 고정
wordcloud(words = df_word$word,    #단어
          freq = df_word$freq,     #빈도
          min.freq = 2,            #최소 단어 빈도
          max.words = 200,         #표현 단어 수
          random.order = F,        #고빈도 단어 중앙 배치
          rot.per = .1,            #회전 단어 비율
          scale = c(4, 0.3),       #단어 크기 범위
          colors = pal)            #색상 목록
