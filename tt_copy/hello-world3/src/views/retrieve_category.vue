<template>
  <div class="cat">

        <list :posts="info.posts"></list>

  </div>

</template>
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

import List from "@/components/list";
export default {
  name: 'cat',
  components: {
    List
    // HelloWorld
  },
  data(){

    return {
    info :{
      posts:null,
    },
      url :'/category/',
      id : null,
      fullurl:null,
    }
  },
  methods:{

    get_post_data(id_t){
      this.fullurl = this.url+id_t+"/";
      this.$axios.get(this.fullurl).then(
          res => {
            this.$set(this.info,"posts",res.data)
          })
    },

  },
  created() {
    document.title = this.$route.meta.title;

    this.id = this.$route.params.id;
      this.get_post_data(this.id);
  },
  watch:{
    $route(to,from){
      if(to.fullPath!=from.fullPath){
          this.get_post_data(to.params.id);
      }
    }
  }




}
</script>
