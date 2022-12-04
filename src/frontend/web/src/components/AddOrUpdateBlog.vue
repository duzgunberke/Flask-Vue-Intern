<template>
    <div>
        <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Title</th>
      <th scope="col">Update</th>
      <th scope="col">Delete</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>

          <a class="btn btn-warning">Update</a>
      </td>
      <td>          <a class="btn btn-danger">Delete</a>
</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>

          <a class="btn btn-warning">Update</a>
      </td>
      <td>          <a class="btn btn-danger">Delete</a>
</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Larry</td>
      <td>

          <a class="btn btn-warning">Update</a>
      </td>
      <td>          <a class="btn btn-danger">Delete</a>
</td>
    </tr>
  </tbody>
</table>
    
    </div>
    </template>
    
    <script>
    //import {mapGetters} from 'vuex'
    export default{
        name:'AddOrUpdateBlog',
        
    
    }
    </script>