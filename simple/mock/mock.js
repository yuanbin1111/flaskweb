import Mock from 'mockjs'

Mock .Mock('/getNewsList',{
    'list|5':[
        {
            url:'@url',
            title:'@ctitle(5,20)'
        }
    ]
})