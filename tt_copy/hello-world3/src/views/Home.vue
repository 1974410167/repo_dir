<template>
  <div class="home">

    <list :posts="posts"></list>
    <nav aria-label="Page navigation">
      <ul class="pagination">

        <li>

          <a href="#" aria-label="Previous" @click="get_page('previous')">
              <span aria-hidden="true">&laquo;</span>
          </a>
        </li>

        <li><a href="#" @click="get_one_page(1)">1</a></li>
        <li><a href="#" @click="get_one_page(2)">2</a></li>
        <li><a href="#" @click="get_one_page(3)">3</a></li>
        <li><a href="#" @click="get_one_page(4)">4</a></li>
        <li><a href="#" @click="get_one_page(5)">5</a></li>
        <li><a href="#" @click="get_one_page(6)">6</a></li>



          <li>
              <a href="#" aria-label="Next" @click="get_page('next')">
                <span aria-hidden="true">&raquo;</span>
              </a>
          </li>


      </ul>
    </nav>
  </div>

</template>

<script>

import List from "@/components/list";
export default {
  name: 'home',
  components: {
    List
  // HelloWorld
    },
  data(){
    return{
      posts:null,
      previous:null,
      next:null,
      url:'/post/',
      count:null,
      base_url:'/post/',
    }
  },

  created() {

    this.get_page('1');
    document.title = this.$route.meta.title;
    },

  methods:{

    get_page:function (pro){

      if(pro=='next'){
          this.url = this.next;
      }else if(pro=='previous'){
        this.url = this.previous;
      }

      if(this.url==null){
        if(pro=='next'){
          alert("没有下一页了")
        }else if(pro=='previous'){
          alert("没有上一页了")
        }
      }else {
        this.help();
      }

    },

    help(){
      this.$axios.get(this.url).then(
          res => {

            this.posts = res.data.results;
            var p = res.data.previous;
            if (p!=null){
              this.previous = p.slice(0,20)+":5637"+p.slice(20);
            }

            var n = res.data.next;
            if(n!=null){
              this.next = n.slice(0,20)+":5637"+n.slice(20);
            }
            this.count = res.data.count;
          })
    },
    get_one_page(num){
        var page_num = Math.ceil(this.count/6);
        if(num>page_num){
          alert("此页不存在")
        }else{
          this.url = this.base_url+"?page="+num;
          this.help()
        }
    }

  },


}
</script>

