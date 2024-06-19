<script setup>

</script>


<template>
  <el-card  class="pic" style="display: flex; width: 100%; justify-content: center">
    <img :src="imgUrl" alt="图片" width="580" height="580">
  </el-card>
</template>
  
  <script>
  import img from '../pic/超市管理系统欢迎界面.jpg'
  
  export default {
    data() {
      return {
        imgUrl: img
      }
    }
  }
  </script>

<style>
.pic {
  position: relative;
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 10px;
}

</style>

