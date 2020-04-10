<template>
  <div class="con" id="app">
    <h2>shooping list</h2>
    <div class="inp_shop">
      <input class="js-new" type="text" placeholder="you want to buy" />
      <span class="btu">
        <button class="js-add btn btn-default">add shopping</button>
      </span>
    </div>
    <ul>
      <li>
        <div class="checkbox">
          <label for>
            <input class="js-item" type="checkbox" />apple
          </label>
        </div>
      </li>
      <li>
        <div class="checkbox">
          <label for>
            <input class="js-item" type="checkbox" />banana
          </label>
        </div>
      </li>
      <li>
        <div class="checkbox">
          <label for>
            <input class="js-item" type="checkbox" />organ
          </label>
        </div>
      </li>
    </ul>
    <div class="footer">
      <span>change title</span>
      <input type="text" class="js-change" placeholder="shopping list" />
    </div>
  </div>
</template>

<script>
</script>

<style>
.con {
  width: 40%;
  margin: 100px auto;
}
ul {
  border: 1px solid black;
  margin-top: 20px;
}
ul li {
  list-style-type: none;
}
.removed {
  color: gray;
}
.removed label {
  text-decoration: line-through;
}
</style>

