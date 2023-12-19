<template>

  <div class="retrive_tag">
      <list v-bind:posts="info.posts"></list>
  </div>

</template>

<script>
import List from "@/components/list";
export default {
    name: "retrive_tag",
  components: {List},
  data(){

    return {
      info :{
        posts:null,
      },
      url :'/tag/',
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

<style scoped>

</style>