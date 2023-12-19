<template>
  <div class="archives">

    <list :posts="info.posts"></list>

  </div>

</template>
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

import List from "@/components/list";
export default {
  name: 'archives',
  components: {
    List
    // HelloWorld
  },
  data(){

    return {
      info :{
        posts:null,
      },
      url :'/archive/',
      fullurl:null,
      month:null,
      year:null,
    }
  },
  methods:{

    get_post_data(){

      this.fullurl = this.url+this.year+"/"+this.month+"/";
      this.$axios.get(this.fullurl).then(
          res => {
            this.$set(this.info,"posts",res.data)
          })
    },

  },
  created() {



    document.title = this.$route.meta.title;

    this.month = this.$route.params.month;
    this.year = this.$route.params.year;
    this.get_post_data();
  },

  watch:{
    $route(to,from){
      if(to.fullPath!=from.fullPath){
        this.month = to.params.month;
        this.year = to.params.year;
        this.get_post_data();
      }
    }
  }




}
</script>
