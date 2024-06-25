<script>
import ProductList from '@/components/ProductList.vue'; 
import ProductForm from '@/components/ProductForm.vue';  
export default {
  components: {
    ProductList,
    ProductForm,
  },
};

</script>

<template>
  <div class="about">
    <ProductList />
    <ProductForm />
<!--    <h1>This is an about page</h1>-->
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
