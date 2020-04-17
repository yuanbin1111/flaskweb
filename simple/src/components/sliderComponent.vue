<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <!-- 四张轮播图 -->
        <div v-show="nowIndex === index" class="slider-item" v-bind:class="['item'+[index+1]]" v-for='(imgUrl,index) in sliderImgList' v-bind:key='index'>
            <a href="">
                <img v-bind:src="imgUrl" alt="">
            </a>
        </div>

        <!-- 上一张下一张按钮 -->
        <a v-on:click="preHandler" class='btn pre-btn' href="javascript:void(0)">&lt;</a>
        <a v-on:click="nextHandler" class='btn next-btn' href="javascript:void(0)">&gt;</a>

        <!-- 下方的原点 -->
        <ul class="slider-dots">
            <li  v-on:click='clickDots' v-for='(item,index) in sliderImgList' v-bind:key='index'>{{ index+1 }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            nowIndex:0,
            sliderImgList:[
                require('../assets/0.jpg'),
                require('../assets/1.jpg'),
                require('../assets/2.jpg'),
                require('../assets/3.jpg')
            ]
        }
    },
    methods: {
        clickDots(){
            this.nowIndex = index
        },
        preHandler(){
            this.nowIndex--;
            if(this.nowIndex < 0){
                this.nowIndex = 3
            }
        },
        nextHandler(){
            this.autoplay()
        },
        autoplay(){
            this.nowIndex++;
            if(this.nowIndex >3){
                this.nowIndex = 0
            }
        },
        runInv(){
            this.invId = setInterval(this.autoplay,2000)
        },
        clearInv(){
            clearInterval(this.invId)
        }
    },
    created() {
        this.runInv()
    }
}
</script>

<style>
.slider-wrapper{
    width: 900px;
    height: 500px;
    background: red;
    position: relative;
}
.slider-item{
    width: 900px;
    height: 500px;
    text-align: center;
    line-height: 500px;
    font-size: 40px;
    position:absolute;
}
.item1{
    z-index: 100;
}
.item2{
    z-index: 90;
}
.item3{
    z-index: 80;
}
.item4{
    z-index: 70;
}
.slider-dots{
    position: absolute;
    right: 20px;
    bottom: 20px;
    list-style: none;
    z-index: 200;
}
.slider-dots li{
    width: 15px;
    height: 15px;
    border-radius: 50%;
    background: #000;
    color: white;
    text-align: center;
    line-height: 15px;
    float: left;
    margin: 0 10px;
    opacity: 0.6;
}
.btn{
    display: inline-block;
    width: 50px;
    height: 50px;
    color: white;
    background: #000;
    font-size: 40px;
    text-align: center;
    line-height: 50px;
    position: absolute;
    z-index: 300;
    top: 50%;
    margin-top: -25px;
    opacity: 0.6;
}
.pre-btn{
    left: 10px;
}
.next-btn{
    right: 10px;
}
</style>