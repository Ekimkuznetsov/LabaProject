# Task2

Module 6. Thems 2.HTTP & curl Исследование HTTP протокола 
1.Найти в интернете 8 различных status code HTTP. 
В запросе и ответе должно содержаться не менее 5 header’s атрибутов. 
2.Описать назначение всех атрибутов в client request and server response. 
На примере одного из HTTP request/response описать все header’s атрибуты. 
3.Найти еще 7 различных status code. Выполнять только после выполнения задания 1. 
4.Произвести фильтрацию трафика протокола HTTP с помощью tcpdump. 
Написать два фильтра: a.фильтровать по методам протокола HTTP.  
b.фильтровать по методу и header’s атрибуту в response протокола HTTP 
c.фильтровать по методу и header’s атрибуту в request протокола HTTP 
5.Используя Fiddler выполнить пункт 4. 
6.Используя Fiddler попробовать вскрыть HTTPs. 
curl -o - -I http://google.com

## 2.1
1.Найти в интернете 8 различных status code HTTP. 
В запросе и ответе должно содержаться не менее 5 header’s атрибутов. 

curl -o - -I http://google.com

-I, --head
              (HTTP  FTP FILE) Fetch the headers only! HTTP-servers feature the command HEAD which this uses to get nothing but the header of a document. When used on an FTP or FILE file, curl dis‐
              plays the file size and last modification time only.
-o, --output <file>
              Write output to <file> instead of stdout. If you are using {} or [] to fetch multiple documents, you can use '#' followed by a number in the <file> specifier. That  variable  will  be
              replaced with the current string for the URL being fetched. Like in:

               curl http://{one,two}.example.com -o "file_#1.txt"


curl -o - -I http://www.get.club/
1) HTTP/1.1 301 Moved Permanently
Server: nginx
Date: Sun, 03 Jul 2022 19:01:53 GMT
Content-Type: text/html
Content-Length: 162
Connection: keep-alive
Keep-Alive: timeout=20
Location: http://get.club/
2) HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 3094
Connection: keep-alive
Last-Modified: Thu, 18 Apr 2019 15:50:45 GMT
Server: AmazonS3
Date: Sun, 03 Jul 2022 11:59:03 GMT
ETag: "d1264f85cadffb73ba7ac63c980e3381"
X-Cache: Hit from cloudfront
Via: 1.1 40b77149d6ba01da8c2f52c235bceed0.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: BUD50-C1
X-Amz-Cf-Id: oDrqcxhPzREntswMWxq4jtH6X8g8JkEskyAP_17aXN_ZMLGzgCOEiw==
3) HTTP/1.1 302 Found
Date: Sun, 03 Jul 2022 19:07:38 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
X-StatusPage-Version: 495985d5c0beed935b8974df703040405edfbff5
Vary: Accept,Accept-Encoding,X-Forwarded-Host,X-Forwarded-Scheme,X-Forwarded-Proto,Fastly-SSL
Strict-Transport-Security: max-age=259200
X-StatusPage-Skip-Logging: true
Location: https://status.recurly.com/
Cache-Control: no-cache
X-Request-Id: b43bf061-9767-479e-af80-e50d10b827ef
X-Runtime: 0.024918
Age: 0
X-Cache: MISS
4) 



