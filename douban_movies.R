# install.packages("rvest")
library(rvest)
library(magrittr)
url ='https://movie.douban.com/cinema/nowplaying/guangzhou/'

web = url %>% 
  read_html(encoding='UTF-8') %>% 
  html_nodes('li.list-item')

title=web %>% html_nodes('li.stitle>a[title]') %>% 
  html_attr('title')

actors=web %>%
  html_attr('data-actors')

director=web %>%
  html_attr('data-director')

region=web %>%
  html_attr('data-region')

score= web %>%
  html_attr('data-score')

data=data.frame(title=title,
                actors=actors,
                director=director,
                region=region,
                score=score)

head(data)
