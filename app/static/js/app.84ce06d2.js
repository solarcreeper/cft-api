(function(e){function t(t){for(var a,s,l=t[0],i=t[1],c=t[2],p=0,f=[];p<l.length;p++)s=l[p],Object.prototype.hasOwnProperty.call(n,s)&&n[s]&&f.push(n[s][0]),n[s]=0;for(a in i)Object.prototype.hasOwnProperty.call(i,a)&&(e[a]=i[a]);u&&u(t);while(f.length)f.shift()();return o.push.apply(o,c||[]),r()}function r(){for(var e,t=0;t<o.length;t++){for(var r=o[t],a=!0,l=1;l<r.length;l++){var i=r[l];0!==n[i]&&(a=!1)}a&&(o.splice(t--,1),e=s(s.s=r[0]))}return e}var a={},n={app:0},o=[];function s(t){if(a[t])return a[t].exports;var r=a[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,s),r.l=!0,r.exports}s.m=e,s.c=a,s.d=function(e,t,r){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(s.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)s.d(r,a,function(t){return e[t]}.bind(null,a));return r},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/";var l=window["webpackJsonp"]=window["webpackJsonp"]||[],i=l.push.bind(l);l.push=t,l=l.slice();for(var c=0;c<l.length;c++)t(l[c]);var u=i;o.push([0,"chunk-vendors"]),r()})({0:function(e,t,r){e.exports=r("56d7")},"0dae":function(e,t,r){},"142a":function(e,t,r){e.exports=r.p+"img/cft.b57b212c.png"},"22a1":function(e,t,r){"use strict";var a=r("28fe"),n=r.n(a);n.a},"28fe":function(e,t,r){},"36fe":function(e,t,r){"use strict";var a=r("0dae"),n=r.n(a);n.a},"56d7":function(e,t,r){"use strict";r.r(t);r("e260"),r("e6cf"),r("cca6"),r("a79d");var a=r("2b0e"),n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{attrs:{id:"app"}},[r("router-view")],1)},o=[],s={name:"app"},l=s,i=r("2877"),c=Object(i["a"])(l,n,o,!1,null,null,null),u=c.exports,p=r("8c4f"),f=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"login_container"},[r("div",{staticClass:"login_box"},[e._m(0),r("el-form",{ref:"loginFormRef",staticClass:"login_form",attrs:{model:e.loginForm,rules:e.loginFormRules}},[r("el-form-item",{attrs:{prop:"username"}},[r("el-input",{attrs:{"prefix-icon":"el-icon-user-solid"},model:{value:e.loginForm.username,callback:function(t){e.$set(e.loginForm,"username",t)},expression:"loginForm.username"}})],1),r("el-form-item",{attrs:{prop:"password"}},[r("el-input",{attrs:{"refix-icon":"el-icon-lock",type:"password"},model:{value:e.loginForm.password,callback:function(t){e.$set(e.loginForm,"password",t)},expression:"loginForm.password"}})],1),r("el-form-item",{staticClass:"btns"},[r("el-button",{attrs:{type:"primary"},on:{click:function(t){return e.submitForm("loginFormRef")}}},[e._v("登陆")]),r("el-button",{attrs:{type:"info"},on:{click:function(t){return e.resetForm("loginFormRef")}}},[e._v("重置")])],1)],1)],1)])},d=[function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"avatar_box"},[a("img",{attrs:{src:r("cf05"),alt:""}})])}],m={data:function(){return{loginForm:{username:"admin",password:"12345"},loginFormRules:{username:[{required:!0,message:"请输入用户名",trigger:"blur"},{min:5,max:12,message:"长度在 5 到 12 个字符",trigger:"blur"}],password:[{required:!0,message:"请输入密码",trigger:"blur"}]}}},methods:{resetForm:function(e){this.$refs[e].resetFields()},submitForm:function(e){var t=this;this.$refs[e].validate((function(e){e&&("admin"===t.loginForm.username&&"12345"===t.loginForm.password?(window.sessionStorage.setItem("token","test"),t.$message({showClose:!0,message:"login success",type:"success",duration:1e3}),t.$router.push("/home")):t.$message({showClose:!0,message:"login failed",type:"error",duration:1e3}))}))}}},h=m,b=(r("22a1"),Object(i["a"])(h,f,d,!1,null,"74fb810c",null)),g=b.exports,_=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("el-container",{staticClass:"home-container"},[a("el-header",[a("div",[a("img",{staticClass:"logo",attrs:{src:r("142a"),alt:""}}),a("span",[e._v("自动化测试平台")])]),a("el-button",{attrs:{type:"info"},on:{click:e.logout}},[e._v("quit")])],1),a("el-container",[a("el-aside",{attrs:{width:"200px"}},[a("el-menu",{attrs:{"background-color":"#333744","text-color":"#fff","active-text-color":"#409fff",router:!0}},e._l(e.menulist,(function(t){return a("el-menu-item",{key:t.path,attrs:{index:t.path}},[a("template",{slot:"title"},[a("i",{class:t.icon}),a("span",{staticClass:"item-text"},[e._v(e._s(t.text))])])],2)})),1)],1),a("el-main",[a("router-view")],1)],1)],1)},v=[],w={data:function(){return{menulist:[{path:"io",text:"IO模型库",icon:"el-icon-coin"},{path:"result",text:"执行结果",icon:"el-icon-notebook-2"},{path:"task",text:"任务列表",icon:"el-icon-notebook-1"},{path:"config",text:"任务配置",icon:"el-icon-s-tools"},{path:"report",text:"测试报告",icon:"el-icon-s-data"}]}},methods:{logout:function(){window.sessionStorage.clear(),this.$message({showClose:!0,message:"logout success",type:"success",duration:1e3}),this.$router.push("/login")}}},y=w,x=(r("72a5"),Object(i["a"])(y,_,v,!1,null,"0972b46a",null)),O=x.exports,$=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"content-wrapper"},[r("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[r("el-breadcrumb-item",{attrs:{to:{path:"/home"}}},[e._v("首页")]),r("el-breadcrumb-item",[e._v("Welcome")])],1),r("el-card")],1)},k=[],C={},q=C,j=Object(i["a"])(q,$,k,!1,null,"e16d0820",null),F=j.exports,I=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"content-wrapper"},[r("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[r("el-breadcrumb-item",{attrs:{to:{path:"/home"}}},[e._v("首页")]),r("el-breadcrumb-item",[e._v("IO模型库")])],1),r("el-card",{staticClass:"box-card"},[r("el-row",{attrs:{gutter:30}},[r("el-col",{attrs:{span:4}},[r("el-input",{attrs:{placeholder:"IO名称"},on:{change:e.search},model:{value:e.query_info.io_name,callback:function(t){e.$set(e.query_info,"io_name",t)},expression:"query_info.io_name"}})],1),r("el-col",{attrs:{span:4}},[r("el-input",{attrs:{placeholder:"IO工具"},on:{change:e.search},model:{value:e.query_info.tool_name,callback:function(t){e.$set(e.query_info,"tool_name",t)},expression:"query_info.tool_name"}})],1),r("el-col",{attrs:{span:6}},[r("el-input",{attrs:{placeholder:"IO参数"},on:{change:e.search},model:{value:e.query_info.io_params,callback:function(t){e.$set(e.query_info,"io_params",t)},expression:"query_info.io_params"}})],1),r("el-col",{attrs:{span:2,push:3}},[r("el-button",{attrs:{type:"primary"},on:{click:e.clear}},[e._v("清除")])],1),r("el-col",{attrs:{span:2,push:3}},[r("el-button",{attrs:{type:"success"}},[e._v("新建")])],1),r("el-col",{attrs:{span:2,push:3}},[r("el-button",{attrs:{type:"danger"},on:{click:e.remove}},[e._v("删除")])],1)],1),r("el-row",[r("el-table",{attrs:{data:e.io_list,border:"",stripe:""},on:{"selection-change":e.handleSelectionChange}},[r("el-table-column",{attrs:{type:"selection",width:"35"}}),r("el-table-column",{attrs:{prop:"io_name",label:"IO名称",width:"140"}}),r("el-table-column",{attrs:{prop:"tool_name",label:"IO工具",width:"140"}}),r("el-table-column",{attrs:{prop:"io_params",label:"IO参数"}})],1)],1),r("el-pagination",{attrs:{"current-page":e.query_info.page,"page-sizes":[30,50,100],"page-size":e.query_info.per_page,layout:"total, sizes, prev, pager, next, jumper",total:e.total},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1)],1)},S=[],E=(r("a4d3"),r("e01a"),r("d28b"),r("d3b7"),r("3ca3"),r("ddb0"),r("96cf"),r("1da1")),M={data:function(){return{query_info:{io_name:"",tool_name:"",io_params:"",page:1,per_page:30},io_list:[],selected_io_list:[],total:0}},created:function(){this.getIOModuleList()},methods:{getIOModuleList:function(){var e=this;return Object(E["a"])(regeneratorRuntime.mark((function t(){var r,a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,e.$http.get("io",{params:e.query_info});case 2:if(r=t.sent,a=r.data,!0===a.result){t.next=6;break}return t.abrupt("return",e.$message({showClose:!0,message:"获取IO模型库失败",type:"error",duration:1e3}));case 6:e.io_list=a.data,e.total=a.total;case 8:case"end":return t.stop()}}),t)})))()},handleSizeChange:function(e){this.query_info.per_page=e,this.getIOModuleList()},handleCurrentChange:function(e){this.query_info.page=e,this.getIOModuleList()},handleSelectionChange:function(e){this.selected_io_list=e},search:function(){this.getIOModuleList()},clear:function(){this.query_info.page=1,this.query_info.io_name="",this.query_info.tool_name="",this.query_info.io_params="",this.getIOModuleList()},remove:function(){var e=this;return Object(E["a"])(regeneratorRuntime.mark((function t(){var r,a,n,o,s,l,i,c,u;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(0!==e.selected_io_list.length){t.next=2;break}return t.abrupt("return",e.$message({message:"请选择需要删除得模型",type:"error",duration:1e3}));case 2:r=!0,a=!1,n=void 0,t.prev=5,o=e.selected_io_list[Symbol.iterator]();case 7:if(r=(s=o.next()).done){t.next=18;break}return l=s.value,i={io_name:l.io_name},t.next=12,e.$http.delete("io",{params:i});case 12:c=t.sent,u=c.data,!0!==u.result?e.$message({message:"删除IO模型失败",type:"error",duration:300}):e.$message({message:"删除IO模型成功",type:"success",duration:300});case 15:r=!0,t.next=7;break;case 18:t.next=24;break;case 20:t.prev=20,t.t0=t["catch"](5),a=!0,n=t.t0;case 24:t.prev=24,t.prev=25,r||null==o.return||o.return();case 27:if(t.prev=27,!a){t.next=30;break}throw n;case 30:return t.finish(27);case 31:return t.finish(24);case 32:e.getIOModuleList();case 33:case"end":return t.stop()}}),t,null,[[5,20,24,32],[25,,27,31]])})))()}}},R=M,L=(r("36fe"),Object(i["a"])(R,I,S,!1,null,"20d1c499",null)),P=L.exports,z=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"content-wrapper"},[r("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[r("el-breadcrumb-item",{attrs:{to:{path:"/home"}}},[e._v("首页")]),r("el-breadcrumb-item",[e._v("执行结果")])],1),r("el-card")],1)},T=[],J={},U=J,W=Object(i["a"])(U,z,T,!1,null,"2abbfdec",null),A=W.exports,B=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"content-wrapper"},[r("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[r("el-breadcrumb-item",{attrs:{to:{path:"/home"}}},[e._v("首页")]),r("el-breadcrumb-item",[e._v("任务列表")])],1),r("el-card")],1)},D=[],G={},H=G,K=Object(i["a"])(H,B,D,!1,null,"591934d6",null),N=K.exports,Q=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"content-wrapper"},[r("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[r("el-breadcrumb-item",{attrs:{to:{path:"/home"}}},[e._v("首页")]),r("el-breadcrumb-item",[e._v("任务配置")])],1),r("el-card")],1)},V=[],X={},Y=X,Z=Object(i["a"])(Y,Q,V,!1,null,"30ef3929",null),ee=Z.exports,te=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"content-wrapper"},[r("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[r("el-breadcrumb-item",{attrs:{to:{path:"/home"}}},[e._v("首页")]),r("el-breadcrumb-item",[e._v("测试报告")])],1),r("el-card")],1)},re=[],ae={},ne=ae,oe=Object(i["a"])(ne,te,re,!1,null,"bffb37e2",null),se=oe.exports;a["default"].use(p["a"]);var le=[{path:"/login",component:g},{path:"/",redirect:"/login"},{path:"/home",component:O,redirect:"/welcome",children:[{path:"/welcome",component:F},{path:"/io",component:P},{path:"/result",component:A},{path:"/task",component:N},{path:"/config",component:ee},{path:"/report",component:se}]}],ie=new p["a"]({routes:le});ie.beforeEach((function(e,t,r){if("/login"===e.path)return r();var a=window.sessionStorage.getItem("token");if(!a)return r("/login");r()}));var ce=ie,ue=(r("0fb7"),r("450d"),r("f529")),pe=r.n(ue),fe=(r("672e"),r("101e")),de=r.n(fe),me=(r("5466"),r("ecdf")),he=r.n(me),be=(r("38a0"),r("ad41")),ge=r.n(be),_e=(r("f4f9"),r("c2cc")),ve=r.n(_e),we=(r("7a0f"),r("0f6c")),ye=r.n(we),xe=(r("b8e0"),r("a4c4")),Oe=r.n(xe),$e=(r("b84d"),r("c216")),ke=r.n($e),Ce=(r("8f24"),r("76b9")),qe=r.n(Ce),je=(r("8bd8"),r("4cb2")),Fe=r.n(je),Ie=(r("34db"),r("3803")),Se=r.n(Ie),Ee=(r("ce18"),r("f58e")),Me=r.n(Ee),Re=(r("4ca3"),r("443e")),Le=r.n(Re),Pe=(r("de31"),r("c69e")),ze=r.n(Pe),Te=(r("a769"),r("5cc3")),Je=r.n(Te),Ue=(r("a673"),r("7b31")),We=r.n(Ue),Ae=(r("adec"),r("3d2d")),Be=r.n(Ae),De=(r("10cb"),r("f3ad")),Ge=r.n(De),He=(r("eca7"),r("3787")),Ke=r.n(He),Ne=(r("425f"),r("4105")),Qe=r.n(Ne),Ve=(r("1951"),r("eedf")),Xe=r.n(Ve);a["default"].use(Xe.a),a["default"].use(Qe.a),a["default"].use(Ke.a),a["default"].use(Ge.a),a["default"].use(Be.a),a["default"].use(We.a),a["default"].use(Je.a),a["default"].use(ze.a),a["default"].use(Le.a),a["default"].use(Me.a),a["default"].use(Se.a),a["default"].use(Fe.a),a["default"].use(qe.a),a["default"].use(ke.a),a["default"].use(Oe.a),a["default"].use(ye.a),a["default"].use(ve.a),a["default"].use(ge.a),a["default"].use(he.a),a["default"].use(de.a),a["default"].prototype.$message=pe.a;r("aede");var Ye=r("bc3a"),Ze=r.n(Ye);Ze.a.defaults.baseURL="http://localhost:8088/cft/api/v1/",Ze.a.interceptors.request.use((function(e){return e})),a["default"].prototype.$http=Ze.a,a["default"].config.productionTip=!1,new a["default"]({router:ce,render:function(e){return e(u)}}).$mount("#app")},"72a5":function(e,t,r){"use strict";var a=r("a28a"),n=r.n(a);n.a},a28a:function(e,t,r){},aede:function(e,t,r){},cf05:function(e,t,r){e.exports=r.p+"img/logo.82b9c7a5.png"}});
//# sourceMappingURL=app.84ce06d2.js.map