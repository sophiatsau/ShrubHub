import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import { authenticate } from "./store/session";

import Navigation from "./components/Navigation";
import Landing from "./components/Landing";
import ShopDetails from "./components/ShopDetails";
import ShopsViewCurrent from "./components/ShopsViewCurrent";
import ShopCreateForm from "./components/ShopCreateForm";
import ShopEditForm from "./components/ShopEditForm";
import ShopByCategory from "./components/ShopByCategory";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/">
            <Landing />
          </Route>
          <Route exact path="/shops/:shopId([0-9]{1,})">
            <ShopDetails />
          </Route>
          <Route exact path="/shops/current">
            <ShopsViewCurrent />
          </Route>
          <Route exact path="/shops/new">
            <ShopCreateForm />
          </Route>
          <Route exact path="/shops/:shopId([0-9]{1,})/edit">
            <ShopEditForm />
          </Route>
          <Route exact path="/shops/:category">
            <ShopByCategory />
          </Route>
          <Route>404 Page Not Found</Route>
        </Switch>
      )}
    </>
  );
}

export default App;
