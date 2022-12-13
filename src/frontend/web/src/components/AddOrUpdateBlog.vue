<template>
  <div>
    <form>
  <!-- Name input -->
  <div class="form-outline mb-4">
    <label class="form-label" for="title">Title</label>
    <input type="text" id="title" class="form-control" />
  </div>

  <!-- Description input -->
  <div class="form-outline mb-4">
    <label class="form-label" for="description">Description</label>
    <textarea class="form-control" id="description" rows="4"></textarea>
  </div>


  <!-- Submit button -->
  <button type="submit" class="btn btn-primary btn-block mb-4">Send</button>
</form>

  </div>
</template>
    
<script>
//import {mapGetters} from 'vuex'
export default {
  name: 'AddOrUpdateBlog',


}
</script>