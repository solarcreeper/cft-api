<template>
  <el-container class="home-container">
    <el-header>
      <div>
        <img class="logo" src="../assets/cft.png" alt />
        <span>自动化测试平台</span>
      </div>
      <el-button type="info" v-on:click="logout">quit</el-button>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-menu background-color="#333744" text-color="#fff" active-text-color="#409fff" v-bind:router="true">
          <el-menu-item v-bind:index="item.path" v-for="item in menulist" v-bind:key="item.path">
            <template slot="title">
              <i v-bind:class="item.icon"></i>
              <span class="item-text">{{item.text}}</span>
            </template>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      menulist: [
        {
          path: 'io',
          text: 'IO模型库',
          icon: 'el-icon-coin'
        },
        {
          path: 'result',
          text: '执行结果',
          icon: 'el-icon-notebook-2'
        },
        {
          path: 'task',
          text: '任务列表',
          icon: 'el-icon-notebook-1'
        },
        {
          path: 'config',
          text: '任务配置',
          icon: 'el-icon-s-tools'
        },
        {
          path: 'report',
          text: '测试报告',
          icon: 'el-icon-s-data'
        }
      ]
    }
  },
  methods: {
    logout () {
      window.sessionStorage.clear()
      this.$message({ showClose: true, message: 'logout success', type: 'success', duration: 1000 })
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="less" scoped>
.home-container {
  height: 100%;
}
.el-header {
  background-color: #373d51;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 10px;
    }
  }
}
.el-aside {
  background-color: #333744;
  .el-menu {
    border-right: none;
  }
}
.el-main {
  background-color: #eaedf1;
}
.logo {
  width: 100px;
}
.item-text {
  margin-left: 2px;
}
</style>
