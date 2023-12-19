<template>
  <div class="about">

    <div v-for="(item,i) in this.text" :key="i">
      <p style="color: #777;font-size:1.5em">{{ item.text }}</p>
    </div>


    <hr>
    <p style="color: #777;font-size:1.5em"><a href="https://github.com/1974410167">email&nbsp;:&nbsp;1974410167@qq.com</a></p>
    <p style="color: #777;font-size:1.5em"><a href="https://github.com/1974410167">github&nbsp;:&nbsp;https://github.com/1974410167</a></p>

  </div>
</template>

<script>

export default {
  name: 'archives',
  data(){
    return {
      url:"/about/",
      text:null,
    }
  },
  created() {
    document.title = this.$route.meta.title;
    this.$axios.get(this.url).then(
        res => {
          this.text = res.data
        })
  }
}
</script>

<style>

  .about p a{
    text-decoration: none;

    color: #777;
  }
</style>