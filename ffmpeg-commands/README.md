# ffmpeg-commands
자주 쓸 법한 ffmpeg 명령어들을 나열해두고 테스트할 수 있는 간단한 영상을 올렸습니다.

## 하는 일
자주 쓰는 ffmpeg 명령어 모음.

## 실행법
ffmpeg 설치는 http://ffmpeg.org/download.html 에서 합니다. 아래 명령어들을 적당히 복사해서 씁니다.

### 기본
```
ffmpeg -i <input> <params...> <output>
``` 
- 주의) 파라미터의 순서(특히 -i 이전)에 따라 동작이 달라질 수 도 있습니다

### 구간 자르기
```
-ss <start> -t <duration> -c:v libx264 -c:a aac -b:a 128k
```
```
ffmpeg -i bbb.mp4 -ss 00:00:00 -t 00:00:05 -c:v libx264 -c:a aac -b:a 128k bbb-1.mp4
```
- 코덱과 비트레이트는 ```ffmpeg -i <input>```만 돌리고 확인한 뒤 동일하게 맞춰주는 것을 권장합니다.

### 해상도 변경
```
-vf scale=960:540
```
```
ffmpeg -i bbb.mp4 -vf scale=960:540 bbb-2.mp4
```
- 16:9 해상도 링크 : https://ko.wikipedia.org/wiki/16:9

### 프레임 추출
```
%04d.jpg
```
```
ffmpeg -i bbb.mp4 ./bbb-3/%04d.png
```
- Output을 저런 형태로 지정하면 알아서 인코딩 됩니다.
- 출력 이미지 포맷 등은 다음 링크를 참조 : https://en.wikibooks.org/wiki/FFMPEG_An_Intermediate_Guide/image_sequence

### 다른 포맷으로 변경
```
<output>.<format>
```
```
ffmpeg -i bbb.mp4 bbb-4.webm
```
- 포맷을 지정하고 싶다면 -v, -a 등으로 코덱을 지정할 것

### 4chan 업로드 포맷
```
-an
```
```
ffmpeg -i bbb.mp4 -an -crf 33 -threads 8 bbb-5.webm
```
- WebM
- 오디오 제거 필수
- 해상도를 줄이거나 ```-framerate 30``` 등으로 프레임을 낮추길 권장
- 참고 : http://wiki.webmproject.org/ffmpeg/vp9-encoding-guide

### gif 만들기
```
-r 15 -vf scale=640:360
```
```
ffmpeg -i bbb.mp4 -r 15 -vf scale=640:360 bbb-6.gif
```
- gif는 어차피 256개 컬러팔레트를 사용해서 색이 늘어날 순 없음
- gif는 포맷상 컬러팔레트 + 해상도 각 픽셀에 비례하므로 해상도를 줄이는게 가장 유효함
- 부드럽게만 보이면 성공, 색이 너무 깨지면 화면 자체의 색상이 줄어들도록 해상도를 줄이거나 구간을 조절해볼 것

## 예제
- [bbb.mp4](bbb.mp4)
- 깃헙 10MB 제한에 맞춰 잘라뒀습니다.
- Big Buck Bunny 출처 : http://bbb3d.renderfarming.net/download.html

## 결과물
- bbb-1 : 구간 자르기
- bbb-2 : 해상도 변경
- bbb-3 : 프레임 추출
- bbb-4 : 다른 포맷 변경
- bbb-5 : 4chan 업로드 포맷
- bbb-6 : gif

## 요구사항
- Windows10
- ffmpeg이 필요합니다.
