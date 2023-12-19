<template>
  <div id="app">

    <body>
    <header>

      <nav class="navbar navbar-default" id="navbar">
        <div class="container">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#header-navbar" aria-expanded="false">
              <span class="sr-only"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>

            <h1 class="logo">
              <router-link to="/">
              <a href="#">HYuan</a>
              </router-link>
            </h1>

          </div>
          <div class="collapse navbar-collapse" id="header-navbar">


            <ul class="nav navbar-nav navbar-right">

              <li><a><router-link to="/">首页</router-link></a></li>
              <li><a><router-link to="/about">关于</router-link></a></li>

            </ul>

          </div>
        </div>
      </nav>
    </header>

    <div class="container">
      <div class="introBanner" v-for="(item,i) in this.sign" :key="i">
        <p style="color: #777">{{ item.text }}</p>
      </div>

      <div class="content-wrap">
        <div class="content">

          <router-view></router-view>


        </div>


        <div class="sidebar">

          <div class="widget widget_hot">
            <h2 class="my_recent">最新文章</h2>

              <ul>

                <div v-for="post in recently_post" :key="post.id">
                  <router-link :to="{name:'ret_post',params:{id:post.id}}">
                    <li>

                      <a title="" href="#">

                        <span class="text">
                          {{ post.title }}
                        </span>

                        <span class="muted"><i class="glyphicon glyphicon-time"></i>
                                            {{  post.create_time.split(".")[0].slice(0,16) }}
                        </span>

                        <span class="muted"><i class="glyphicon glyphicon-eye-open"></i>
                          {{ post.pageviews }}
                        </span>

                        </a>
                    </li>
                  </router-link>
                </div>

            </ul>

          </div>

          <div class="widget widget_category">
            <h3>文章分类</h3>

            <ul>
              <a v-for="cate in all_category" :key="cate.id">

                <router-link :to="{name:'retrieve_category',params:{id:cate.id}}" :key="$route.fullPath">
                  <li><a href="#"><span class="text"><i class="glyphicon glyphicon-triangle-right"></i> {{ cate.name }}</span><span class="count">{{ cate.num_cate }}</span></a></li>
                </router-link>

              </a>
            </ul>

          </div>

          <div class="widget">
            <h3>归档</h3>

            <ul>
              <a v-for="archive in show_archives" :key="archive.id">
                <router-link v-bind:to="{name:'archives',
                                         params:{
                                                 year:archive.year,
                                                 month:archive.month,
                                          } }">
                <li><a><span class="text"><i class="glyphicon glyphicon-play-circle"></i> {{ archive.year }}年{{ archive.month }}月</span></a></li>
                </router-link>
              </a>
            </ul>

          </div>

          <div class="widget widget_sentence">
            <h3>标签云</h3>

            <ul>

              <a v-for="tag in all_tags" :key="tag.id">
                <router-link :to="{name:'ret_tag',params: {id:tag.id}}" :key=tag.id>
                <li><a href="#">{{ tag.name }} <span class="badge">{{ tag.num_tag }}</span></a></li>
                </router-link>
              </a>
            </ul>

          </div>

        </div>
      </div>
    </div>

    <div class="footer">
      <div class="container">
        <p>HYuan的个人网站@Copyright 2020-2021</p>
          <p>本网站运行在华为云&nbsp;|&nbsp;豫ICP备2020030480号</p>
      </div>
    </div>

    </body>

  </div>

</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    // Hello
  },
  data(){
    return {

        recently_post: null,
        all_category:null,
        all_tags:null,
        show_archives:null,
        sign:null,

    }
  },
  created() {


    this.$axios.get('/rec_post/').then(
      res => {
        this.recently_post = res.data
    })

    this.$axios.get('/category/').then(
        res => {
          this.all_category = res.data
        })

    this.$axios.get('/tag/').then(
        res => {
          this.all_tags = res.data
        })

    this.$axios.get('/show_are/').then(
        res => {
          this.show_archives = res.data.data
        })

    this.$axios.get('/sign/').then(
        res => {
          this.sign = res.data
        })

  },


}
</script>

<style scoped>
 @import "assets/css/style.css";
 /*ul li a{*/
 /*"padding-top":30px,*/
 /* "color": #777;*/
 /*}*/
 /*.navbar-default .navbar-nav>li>a {*/
 /*  color: #777;*/
 /*  margin-top:27px;*/
 /*}*/
 /*#header-navbar > ul > li:nth-child(1) > a > a*/
 #header-navbar > ul > li{
   color: #777;
 }
 ul li a a{
   text-decoration: none;
   color: #777;

 }
</style>


