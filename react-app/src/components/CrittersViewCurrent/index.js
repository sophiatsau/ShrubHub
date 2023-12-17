import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { thunkGetUserCritters } from '../../store/critters';

import "./CrittersViewCurrent.css"
import CritterDisplaySection from '../CritterDisplaySection';
import { thunkGetUserShops } from '../../store/shops';

export default function CrittersViewCurrent() {
  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user)
  const critters = useSelector(state => state.critters)
  const shops = useSelector(state => state.shops)

  useEffect(() => {
    if (sessionUser) {
        dispatch(thunkGetUserShops())
        dispatch(thunkGetUserCritters())
    }
  }, [dispatch, sessionUser])

  if (!sessionUser) return <Redirect to="/" />

  const userCritters = sessionUser.critters.map(critterId => critters[critterId])

  if (userCritters.includes(undefined)) return <div>Loading critters...</div>

  const sortedCritters = {};

  sessionUser.shops.forEach(shopId => sortedCritters[shops[shopId].name]=[])

  userCritters.forEach(critter => {
    const shop = sortedCritters[critter.shopName];
    shop.push(critter)
  })

  return (
    <div>
        <h2>Manage Your Critter Inventory</h2>
        <div>
        {
            userCritters.length ?
            Object.entries(sortedCritters).map(([name, critters]) => (
                <div key={name}>
                    <CritterDisplaySection critters={critters} heading={name} />
                </div>
            ))
            : <p>You are not selling any critters.</p>
        }
        </div>
    </div>
  )
}