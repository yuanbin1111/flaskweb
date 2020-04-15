<template>
    <div class="index-wrapper">
        <div class="index-left">
            <!-- 全部产品 -->
            <div class="index-left-block">
                <h2>全部产品</h2>
                <template v-for='product in productList'>
                <h3>{{ product.title }}</h3>
                <ul>
                    <li v-for='item in product.list'>
                        <a v-bind:href="item.url">{{ item.title }}</a>
                    </li>
                </ul>
                <div v-if="product.title == 'PC产品'" class="hr"></div>
                </template>
                
            </div>
            <!-- 最新消息 -->
            <div class="index-left-block lastest-news">
                <h2>最新消息</h2>
                <ul>
                    <li>啦啦啦</li>
                </ul>
            </div>
        </div>
        <div class="index-right">
            <div style="margin:0 auto;width:700px;height:300px;background:blue;">
                使用组件代替
            </div>
            <div class="index-border-list">
                <div class="index-border-item">
                    <h2>第一个标题</h2>
                    <p>第一个的描述</p>
                    <div class="index-border-button">立即购买</div>
                </div>
                <div class="index-border-item">
                    <h2>第二个标题</h2>
                    <p>第二个的描述</p>
                    <div class="index-border-button">立即购买</div>
                </div>
                <div class="index-border-item">
                    <h2>第三个标题</h2>
                    <p>第三个的描述</p>
                    <div class="index-border-button">立即购买</div>
                </div>
                <div class="index-border-item">
                    <h2>第四个标题</h2>
                    <p>第四个的描述</p>
                    <div class="index-border-button">立即购买</div>
                </div>
            </div>
        </div>
    </div>
</template>



<script>
export default {
    data(){
        return{
            productList:{
                pc:{
                    title:'PC产品',
                    list:[
                    {
                        title:'数据统计',
                        url:'http://starcraft.com'
                    },
                    {
                        title:'数据预测',
                        url:'http://warcraft.com'
                    },
                    {
                        title:'流量分析',
                        url:'http://overwatch.com',
                        hot:true
                    },
                    {
                        title:'广告发布',
                        url:'http://hearstone.com'
                    }
                    ]
                },
                app:{
                    title:'手机应用类',
                    list:[
                    {  
                        title:'91助手',
                        url:'http://weixin.com'
                    },
                    {  
                        title:'产品助手',
                        url:'http://weixin.com'
                    },
                    {  
                        title:'智能地图',
                        url:'http://maps.com'
                    },
                    {  
                        title:'语音助手',
                        url:'http://phone.com'
                    }
                    ]     
                }
            }
        };
    }
};
</script>



<style scoped>
    .index-wrapper{
        display:flex;
    }
    .index-left{
        width: 30%;
    }
    .index-right{
        width: 70%;
    }
    .index-left-block{
        margin: 15px;
        background: #fff;
        border-radius:10px;
        box-shadow: 0 0 1px #ddd;
    }
    .index-left-block .hr{
        border-bottom: 1px solid black;
        margin: 20px 0;
    }
    .index-left-block h2{
        background: #4fc08d;
        color:#fff;
        padding: 10px 15px;
        margin-bottom: 20px;
    }
    .index-left-block h3{
        color: black;
        font-weight: bolder;
        padding: 0 15px 5px 15px;
    }
    .index-left-block ul{
        padding: 10px 15px;
    }
    .index-left-block li{
        padding: 5px;
        list-style-type: none;
    }
    .index-border-list{
        display: flex;
        flex-wrap: wrap;
        margin-top: 20px;
        justify-content: center;
    }
    .index-border-item{
        width:30%;
        background: ddd;
        padding-left: 120px;
        height: 125px;
        margin-right: 1%;
        box-shadow: 0 0 1px #ddd;
        margin-bottom: 20px;
        border-radius: 0 0 10px 10px;
    }
    a{
        text-decoration: none;
    }
    
</style>