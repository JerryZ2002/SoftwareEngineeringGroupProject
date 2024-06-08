<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import {useRouter} from "vue-router";
const router = useRouter();
router.push({
  path: "/home"
});

import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
// Before


// After
const handleOpen = (key, keyPath) => {
  console.log(key, keyPath);
}

const handleClose = (key, keyPath) => {
  console.log(key, keyPath);
}

</script>

<template>
<!--  <header>-->
  <div class="home-container">
    <div class="common-layout">
      <el-container>
        <el-header style="display: flex; justify-content: center; align-items: center;margin-left: 120px;">
          <HelloWorld msg="超市仓库管理系统" />
        </el-header>
        <el-container>
          <el-aside class="el-aside" width="220px" max-height="630px" style="flex: 0 0 150px; width: 100%; border: 1px solid #ddd; border-radius: 10px;" >
            <el-row class="tac">
              <el-col class="el-col-12" :span="12" style="width: 100%">
                <el-menu
                    :default-active="$route.name"
                    class="el-menu-vertical-demo"
                    @open="handleOpen"
                    @close="handleClose"
                    :router="true"
                >
                  <el-menu-item index="1" route="/home">
                    <el-icon><location /></el-icon>
                    主界面
                  </el-menu-item>

                  <el-menu-item index="2" route="/PurchaseOrder">
                    <el-icon><document /></el-icon>
                    采购订单
                  </el-menu-item>

                  <el-menu-item index="3" route="/Products">
                    <el-icon><icon-menu /></el-icon>
<!--                    <RouterLink to="/Products" :class="{'active-link': $route.path === '/Products', 'inactive-link': $route.path !== '/Products'}">商品信息</RouterLink>-->
                    商品信息
                  </el-menu-item>
                  <el-menu-item index="4" route="/SalesOrder">
                    <el-icon><document /></el-icon>
<!--                    <RouterLink to="/SalesOrder" :class="{'active-link': $route.path === '/SalesOrder', 'inactive-link': $route.path !== '/SalesOrder'}">销售订单</RouterLink>-->
                    销售订单
                  </el-menu-item>
                  <el-menu-item index="5" route="/Inventories">
                    <el-icon><setting /></el-icon>
<!--                    <RouterLink to="/Inventories" :class="{'active-link': $route.path === '/Inventories', 'inactive-link': $route.path !== '/Inventories'}">库存   </RouterLink>-->
                    库存
                  </el-menu-item>
                </el-menu>
              </el-col>
            </el-row>
            <!--          <nav>-->
            <!--            <RouterLink to="/home">主界面</RouterLink>-->
            <!--            <RouterLink to="/PurchaseOrder">采购订单</RouterLink>-->
            <!--            <RouterLink to="/Products">商品信息</RouterLink>-->
            <!--            <RouterLink to="/SalesOrder">销售订单</RouterLink>-->
            <!--            <RouterLink to="/Inventories">库存</RouterLink>-->
            <!--          </nav>-->
          </el-aside>

          <el-main style="flex: 1; padding: 20px; width: 1000px;">
<!--            <RouterView />-->
            <router-view></router-view>
          </el-main>
        </el-container>
      </el-container>
    </div>
  </div>



</template>

<style scoped>


header {
  line-height: 1.5;
  max-height: 100vh;
}
.home-container {
  background-image: url('/src/pic/R.jpeg');
  background-size: cover;
  background-position: center;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.9);
  color: #333;
}
.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.el-aside{
  height: 660px;
  background-color: rgba(255, 255, 255, 0.9);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.9);
}
.custom-active-link {
  color: #626aef;
  background-color: transparent;
}
.active-link {
  color: #54cafa;
}
.custom-active-link {
  color: #626aef;
  background-color: transparent;
}

.inactive-link {
  color: rgba(168, 149, 149, 0.99);
  background-color: transparent;
}


@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
.el-col-12 {
  max-width: 100%;
  flex: 0 0 100%;
}
</style>
