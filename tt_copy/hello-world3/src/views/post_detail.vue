<template>
  <div class="post_detail">
    <detail :post="post" v-if="condation" :comments="comments"></detail>
  </div>
</template>

<script>
import detail from "@/components/detail";
export default {

  name: "post_detail",
 components:{detail},

  data(){
    return {
      post:null,
      url :'/post/',
      com_end_url:'/comments/',
      id : null,
      fullurl:null,
      sign : null,
      comments:null,
    }
  },
  methods:{

    get_post_data(id_t){

      this.fullurl = this.url+id_t+"/";
      this.$axios.get(this.fullurl).then(
          res => {
            this.post = res.data;
          }).catch(function (err){
        console.log(err);
      })
      },

    get_post_comments(id_t){

      var u = this.url+id_t+this.com_end_url;
      this.$axios.get(u).then(
        res => {
          this.comments = res.data;
        }
      )

  }},

  computed:{
    condation:function (){
      if(this.post===null){
        return false
      }
      else {
        return true
      }
    }
  },

  created() {

    document.title = this.$route.meta.title;
    this.id = this.$route.params.id;
    this.get_post_data(this.id);
    this.get_post_comments(this.id)

  },
  watch:{
    $route(to,from){
      if(to.fullPath!=from.fullPath){
        this.id = to.params.id;
        this.get_post_data(this.id);
        this.get_post_comments(this.id)
      }
    }
  }


}
</script>

<style scoped>

</style>