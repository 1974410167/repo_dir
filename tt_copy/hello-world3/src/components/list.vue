  <template>
    <div class="list">
      <div class="title">
        <h3>最新发布</h3>
      </div>

      <div v-for="post in posts" :key="post.id">
        <div class="excerpt">

          <header>
            <a class="cat" href="#">{{ post.category }}<i></i></a>

            <router-link :to="{name:'ret_post',params:{id:post.id}}">
              <h2><a href="#">{{ post.title }}</a></h2>
            </router-link>

          </header>

          <router-link :to="{name:'ret_post',params:{id:post.id}}" style="    text-decoration: none;color: #777;">
          <p>{{ post.excerpt }}</p>
          </router-link>

          <p class="meta">

            <a v-for="tag in post.tags" v-bind:key="tag.id">
              <a class="category" href="#"><i class="glyphicon glyphicon-folder-open"></i>&nbsp;{{ tag.name }}</a>
            </a>

            <a class="time" href="#"><i class="glyphicon glyphicon-time"></i> {{ post.create_time.split(".")[0].slice(0,16) }}</a>
            <a class="views" href="#"><i class="glyphicon glyphicon-eye-open"></i> {{ post.pageviews }}</a>
            <a class="comment" href="#"><i class="glyphicon glyphicon-comment">{{ post.comments.length }}</i> </a>
          </p>
        </div>
      </div>
    </div>

  </template>

<script>
export default {
  name: "list",
  props:{
    posts:Array,
  }


}
</script>

<style scoped>

</style>