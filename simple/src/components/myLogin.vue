<template>
    <div class="login-wrapper">
        <div style="login-mask" id="mask"></div>
        <div class="ui-dialog" id="dialogMove">
            <div class="ui-dialog-title" id='dialogDrag'>
                用户名密码登录
                <a class='ui-dialog-closebutton' href="javascript:viod(0)">X</a>
            </div>
            <div class="ui-dialog-content">
                <div class="ui-dialog-content-item">
                    <input class='ui-dialog-input' type="text" placeholder='手机/邮箱/用户名'>
                </div>
                <div class="ui-dialog-content-item ui-dialog-password">
                    <input class='ui-dialog-input' type="text" placeholder='密码'>
                </div>
                <div class="ui-dialog-content-item">
                    <a class='ui-dialog-submit' href="">登录</a>
                </div>
                <div class="ui-dialog-content-item">
                    <a href="">忘记密码</a>
                </div>
                <div class="ui-dialog-content-item">
                    <a href="">立即注册</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    /* .login-wrapper{
        display: flex;
        justify-self: center;
    } */
    .ui-dialog{
        width: 400px;
        height: auto;
        position: absolute;
        z-index: 9000;
        top: 50%;
        left: 50%;
        margin-left: -200px;
        border: 1px solid #000;
        background: white;
    }
    .ui-dialog a{
        text-decoration: none;
    }
    .ui-dialog-title{
        height: 48px;
        line-height: 48px;
        padding: 0px 20px;
        color: #535353;
        font-size: 16px;
        border-bottom: 1px solid white;
        background: white;
        cursor: move;
        user-select: none;
    }
    .ui-dialog-closebutton{
        width: 16px;
        height: 16px;
        display: block;
        position: absolute;
        top: 0px;
        right: 20px;
        cursor: pointer;
    }
    .ui-dialog-closebutton:hover{
        color: red;
    }
    .ui-dialog-content{
        padding: 15px;
    }
    .ui-dialog-content-item{
        height: 40px;
        line-height: 40px;
        text-align: right;
        padding-top: 15px;
    }
    .ui-dialog-input{
        width: 100%;
        height: 40px;
        margin: 0px;
        padding:0px;
        border: 1px solid white;
        font-size:16px;
        color: #c1c1c1;
        text-indent: 25px;
        outline: none;
    }
    .ui-dialog-submit{
        display: block;
        width: 100%;
        height: 50px;
        background: blue;
        color: white;
        border: none;
        font-size: 16px;
        outline: none;
        text-align: center;
        line-height: 50px;
        font-weight: bolder;
    }
    .ui-dialog-submit:hover{
        background: cornflowerblue;
    }
    .login-mask{
        width: 100%;
        height: 100%;
        background: #000;
        position: absolute;
        top: 0px;
        left: 0px;
        z-index: 8000;
        opacity: 0.4;
    }
</style>