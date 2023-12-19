<template>

  <div class="detail">

    <header class="article-header">
      <h1 class="article-title"><a href="#">{{ post.title }}</a></h1>
      <div class="article-meta ">
        <span class="item category"><a href="# ">{{ post.category }}</a></span>
        <span class="item time ">{{ post.create_time.split(".")[0].slice(0,16)}}</span>
        <span class="item tags">

          标签：

          <a v-for="tag in post.tags" v-bind:key="tag.id">
            <a href="#">{{ tag.name }}</a>
          </a>
        </span>
        <span class="item views"><i class="glyphicon glyphicon-eye-open"></i> {{ post.pageviews }}</span>
      </div>
    </header>

    <article class="article-content" style="word-break: break-word">
<!--      <div class="markdown-body">-->
            <VueMarkDown :source="post.body">
            </VueMarkDown>
    <!--    </div>-->

    </article>

    <div class="title">
      <h3>评论</h3>
    </div>

    <div class="article-comment">
      <form action="" method="POST">
        <input type="text" class="form-control" placeholder="您的昵称（非必填）" v-model="name">
        <input type="email" class="form-control" placeholder="您的邮箱（非必填）" v-model="email">
        <textarea class="form-control" rows="3" placeholder="您的评论或留言（必填）" v-model="text"></textarea>
        <button type="button" class="btn btn-default" @click="post_comment()">发布评论</button>
      </form>
    </div>

    <div class="postcomments">
      <ol class="commentlist">

        <a v-for="(com,index) in comments" :key="com.id">
        <li class="comment-content"><span class="comment-f">{{ index }}</span>
          <div class="comment-main">
            <p><a class="name" href="#" target="_blank">{{ com.name }}</a><span class="time"> {{ com.created_time }}</span><br>{{ com.text }}</p>
          </div>
        </li>
        </a>



      </ol>
    </div>
  </div>
</template>

<script>
import VueMarkDown from 'vue-markdown'

export default {
  name: "detail",
  props:{
    post:Object,
    comments:Array,
  },
  components:{
    VueMarkDown
  },
  data(){
    return {
      name:"",
      email:"",
      text:'',
      post_id:this.post.id,
    }
  },
  methods:{
    post_comment:function () {
      let name_t = '访客';
      let email_t = 'fangke@qq.com';

      if (this.name == ""&& this.email!="") {
        this.help(this.email,name_t);
      } else if(this.email == "" && this.name!="") {
        this.help(email_t,this.name);
      }else if(this.email=="" && this.name==""){
        this.help(email_t,name_t);
      }else if(this.email!="" && this.name!=""){
        this.help(this.email,this.name)
      }

    },

    help(email,name){

      this.$axios.post('/post/comment/',{
        name:name,
        email:email,
        text:this.text,
        post:this.post_id,
        headers:{
          'Content-Type':'application/x-www-form-urlencoded'
        }
      }).then(function (res){
        var status = res.status;
        if(status==201){
          // this.$router.go(0)
        location.reload()
        }else{
          alert("发布失败")
        }
      }).catch(function (error){
        console.log(error)
      })
    }
  }

}
</script>

<style scoped>

</style>