<template>
  <div class="index-wrapper">
    <div class="index-left">
      <!-- 全部产品 -->
      <div class="index-left-block">
        <h2>全部产品</h2>
        <template v-for="product in productlist">
          <h3>{{ product.title }}</h3>
          <ul>
            <li v-for="item in product.list">
              <a v-bind:href="item.url">{{ item.title}}</a>
              <span v-if="item.hot" style="color:white;background:purple;font-size:13px">HOT</span>
            </li>
          </ul>
          <!-- <div v-if="product.title == 'PC产品'" class="hr"></div> -->
          <div v-if="!product.last" class="hr"></div>
        </template>
      </div>
      <!-- 最新消息 -->
      <div class="index-left-block lastest-news">
        <h2>最新消息</h2>
        <li v-for="item in newList">
          <a v-bind:href="item.url">{{ item.title }}</a>
        </li>
      </div>
    </div>
    <div class="index-right">
      <!-- <div style="line-height:300px;width:900px;height:300px;background:red;margin:0 auto">组件</div> -->
      <SliderComponent></SliderComponent>
      <div class="index-border-list">
        <div class="index-border-item" v-for="item in borderlist">
          <div class="index-border-item-inner">
            <h2>{{ item.title }}</h2>
            <p>{{ item.description }}</p>
            <div class="index-border-button">立即购买</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
            <!-- <h2>第一个产品</h2>
            <p>第一个产品描述</p>
            <div class="index-border-button">立即购买</div>
          </div>
        </div>
        <div class="index-border-item">
          <div class="index-border-item-inner">
            <h2>第二个产品</h2>
            <p>第二个产品描述</p>
            <div class="index-border-button">立即购买</div>
          </div>
        </div>
        <div class="index-border-item">
          <div class="index-border-item-inner">
            <h2>第三个产品</h2>
            <p>第三个产品描述</p>
            <div class="index-border-button">立即购买</div>
          </div>
        </div>
        <div class="index-border-item">
          <div class="index-border-item-inner">
            <h2>第四个产品</h2>
            <p>第四个产品描述</p>
            <div class="index-border-button">立即购买</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template> -->


<script>
import axios from "axios"
import SliderComponent from '../components/sliderComponent'
export default {
  // 注册
  components:{
      SliderComponent
  },
  mounted() {
    //获取数据接口
    axios.post("api/getnewList") //接口  
    .then(res => {   //请求成功
      console.log(res);  //打印
      this.newList = res.data.list;
      })
      .catch(error => {  //请求失败
        console.log(error);
      });
    axios.get("api/getproductlist")
    .then(res => {
      console.log(res);
      this.productlist = res.data;
      })
    .catch(error => {
        console.log(error);
      });
    axios.get("api/getborderlist")
    .then(res => {
      console.log(res);
      this.borderlist = res.data;
      })
    .catch(error => {
      console.log(error)
      })
  },
    data(){
      return{
        newList:[],
        productlist:null,
        borderlist:null
      }
    },
  }
//   data() {
//     return {
//       newsList:[
//         {
//             title:'数据统计',
//             url:'http://starcraft.com'
//         },
//         {
//             title:'数据预测',
//             url:'http://warcraft.com'
//         },
//         {
//             title:'流量分析',
//             url:'http://overwatch.com',
//             hot:true
//         },
//         {
//             title:'广告发布',
//             url:'http://hearstone.com'
//         }
//       ],
//       productList:{
//         pc:{
//           title:'PC产品',
//           list:[
//             {
//               title:'数据统计',
//               url:'http://starcraft.com'
//             },
//             {
//               title:'数据预测',
//               url:'http://warcraft.com'
//             },
//             {
//               title:'流量分析',
//               url:'http://overwatch.com',
//               hot:true
//             },
//             {
//               title:'广告发布',
//               url:'http://hearstone.com'
//             }
//           ]
//         },
//         app:{
//           title:'手机应用类',
//           last:true,
//           list:[
//             {
//               title:'91助手',
//               url:'http://weixin.com'
//             },
//             {
//               title:'产品助手',
//               url:'http://weixin.com',
//               hot:true
//             },
//             {
//               title:'智能地图',
//               url:'http://maps.com'
//             },
//             {
//               title:'语音助手',
//               url:'http://iphone.com',
//               hot:true
//             }
//           ]
//         }
//       }
//     }
//   }
// };
</script>


<style scoped>
.index-wrapper {
  width: 1200px;
  display: flex;
}
.index-left {
  width: 300px;
}
.index-right {
  width: 900px;
  margin-top: 15px;
}
.index-left-block {
  margin: 15px;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0 0 1px #dddddd;
}
.index-left-block .hr {
  border-bottom: 1px solid black;
  margin: 20px 0;
}
.index-left-block h2 {
  background: #4fc08d;
  color: #ffffff;
  padding: 10px 15px;
  margin-bottom: 20px;
}
.index-left-block h3 {
  color: #222;
  font-weight: bolder;
  padding: 0 15px 5px 15px;
}
.index-left-block ul {
  padding: 10px 15px;
}
.index-left-block li {
  padding: 5px;
  list-style-type: none;
}
.index-border-list {
  display: flex;
  flex-wrap: wrap;
  margin-top: 20px;
  justify-content: space-between;
  margin-top: 15px;
}
.index-border-item {
  width: 400px;
  background: #ffffff;
  box-shadow: 0 0 1px #ddd;
  border-radius: 0 0 10px 10px;
  margin-bottom: 20px;
  padding: 20px;
}
.index-border-item-inner {
  height: 125px;
  padding-left: 180px;
  background-image: url(../assets/logo.png);
  background-repeat: no-repeat;
  background-size: 30%;
}
.index-border-item-inner h2 {
  font-size: 18px;
  font-weight: bolder;
  color: #000;
  margin-bottom: 15px;
}
.index-border-item-inner p {
  margin-bottom: 15px;
}
.index-border-button {
  width: 80px;
  height: 40px;
  background: rgb(1, 77, 1);
  color: #ffffff;
  border-radius: 5px;
  text-align: center;
  line-height: 40px;
}
/* .hot-tag {
  color: #ffffff;
  background: purple;
  font-size: 5px; */
/* } */
a{
  text-decoration: none;
}
</style>
